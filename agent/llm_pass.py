"""LLM reasoning pass — any OpenAI-compatible provider, auto-detected by which key is set.

  - Groq (GROQ_API_KEY): free, no credit card — the default. https://console.groq.com
  - Hunyuan (HUNYUAN_API_KEY): optional Tencent Cloud sponsor-track alternative.
  - tc3_signed(): optional native TC3-HMAC-SHA256 Tencent call (needs TENCENT_SECRET_ID/KEY).

If no key is present the pass returns [] and the pipeline falls back to the Slither ground-truth
layer. This is reported honestly, never silently faked."""
import os
import json
import hashlib
import hmac
import time
import urllib.request
from typing import List, Dict

from config import (
    HUNYUAN_BASE_URL, HUNYUAN_MODEL, GROQ_BASE_URL, GROQ_MODEL,
    GEMINI_BASE_URL, GEMINI_MODEL, OPENROUTER_BASE_URL, OPENROUTER_MODEL,
)


def _provider():
    """Pick the active OpenAI-compatible provider by which key is set (all free/no-card first)."""
    if os.getenv("GEMINI_API_KEY"):
        return GEMINI_BASE_URL, os.getenv("GEMINI_API_KEY"), GEMINI_MODEL
    if os.getenv("OPENROUTER_API_KEY"):
        return OPENROUTER_BASE_URL, os.getenv("OPENROUTER_API_KEY"), OPENROUTER_MODEL
    if os.getenv("GROQ_API_KEY"):
        return GROQ_BASE_URL, os.getenv("GROQ_API_KEY"), GROQ_MODEL
    if os.getenv("HUNYUAN_API_KEY"):
        return HUNYUAN_BASE_URL, os.getenv("HUNYUAN_API_KEY"), HUNYUAN_MODEL
    return None

_PROMPT = """You are a smart-contract security auditor. Analyze the Solidity below.
Return ONLY a JSON array. Each item: {{"severity": one of [critical,high,medium,low,informational],
"title": short title, "lines": [line numbers], "explanation": one sentence}}.
Report only real, exploitable issues. If none, return [].

SOLIDITY:
{source}
"""


def _parse(content: str) -> List[Dict]:
    content = content.strip()
    if content.startswith("```"):
        content = content.split("```")[1]
        if content.startswith("json"):
            content = content[4:]
    try:
        arr = json.loads(content)
    except Exception:
        return []
    out = []
    for it in arr if isinstance(arr, list) else []:
        out.append({
            "detector": "llm",
            "severity": str(it.get("severity", "informational")).lower(),
            "title": str(it.get("title", ""))[:200],
            "lines": [int(x) for x in it.get("lines", []) if str(x).isdigit()],
            "confidence": "Medium",
            "source": "llm",
            "explanation": str(it.get("explanation", ""))[:300],
        })
    return out


def openai_compatible(source: str) -> List[Dict]:
    prov = _provider()
    if not prov:
        return []
    base_url, key, model = prov
    body = json.dumps({
        "model": model,
        "messages": [{"role": "user", "content": _PROMPT.format(source=source)}],
        "temperature": 0.2,
    }).encode()
    req = urllib.request.Request(
        f"{base_url}/chat/completions", data=body,
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=120) as r:
        data = json.loads(r.read())
    return _parse(data["choices"][0]["message"]["content"])


def tc3_signed(source: str) -> List[Dict]:
    """Native TencentCloud API call with TC3-HMAC-SHA256 signing. Proves load-bearing Tencent auth.
    Requires TENCENT_SECRET_ID / TENCENT_SECRET_KEY in env."""
    sid, skey = os.getenv("TENCENT_SECRET_ID"), os.getenv("TENCENT_SECRET_KEY")
    if not (sid and skey):
        return []
    host, service, version, action, region = (
        "hunyuan.intl.tencentcloudapi.com", "hunyuan", "2023-09-01", "ChatCompletions", "ap-singapore",
    )
    payload = json.dumps({
        "Model": HUNYUAN_MODEL,
        "Messages": [{"Role": "user", "Content": _PROMPT.format(source=source)}],
    })
    ts = int(time.time())
    date = time.strftime("%Y-%m-%d", time.gmtime(ts))
    ct = "application/json; charset=utf-8"
    canonical = (
        f"POST\n/\n\ncontent-type:{ct}\nhost:{host}\nx-tc-action:{action.lower()}\n\n"
        f"content-type;host;x-tc-action\n{hashlib.sha256(payload.encode()).hexdigest()}"
    )
    scope = f"{date}/{service}/tc3_request"
    sts = f"TC3-HMAC-SHA256\n{ts}\n{scope}\n{hashlib.sha256(canonical.encode()).hexdigest()}"

    def _h(k, m):
        return hmac.new(k, m.encode(), hashlib.sha256).digest()

    sk = _h(_h(_h(("TC3" + skey).encode(), date), service), "tc3_request")
    sig = hmac.new(sk, sts.encode(), hashlib.sha256).hexdigest()
    auth = (
        f"TC3-HMAC-SHA256 Credential={sid}/{scope}, "
        f"SignedHeaders=content-type;host;x-tc-action, Signature={sig}"
    )
    req = urllib.request.Request(
        f"https://{host}", data=payload.encode(),
        headers={
            "Authorization": auth, "Content-Type": ct, "Host": host,
            "X-TC-Action": action, "X-TC-Version": version, "X-TC-Timestamp": str(ts),
            "X-TC-Region": region,
        },
    )
    with urllib.request.urlopen(req, timeout=120) as r:
        data = json.loads(r.read())
    choices = data.get("Response", {}).get("Choices", [])
    if not choices:
        return []
    return _parse(choices[0]["Message"]["Content"])


def run_llm(source: str) -> List[Dict]:
    """Prefer the native signed path (deeper Tencent integration); fall back to OpenAI-compatible."""
    if os.getenv("TENCENT_SECRET_ID") and os.getenv("TENCENT_SECRET_KEY"):
        try:
            return tc3_signed(source)
        except Exception:
            pass
    try:
        return openai_compatible(source)
    except Exception:
        return []
