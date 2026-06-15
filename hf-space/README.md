---
title: Sentinel Audit API
emoji: 🛡️
colorFrom: green
colorTo: gray
sdk: docker
app_port: 7860
pinned: false
---

# Sentinel Audit API

Audits any smart contract on demand and returns a security verdict (grade, findings, report hash).
Backs the live demo at https://yonkoo11.github.io/mantle-sentinel/

- `GET /health` — liveness + which LLM provider is active
- `POST /audit` — `{ "address": "0x…" }` or `{ "source": "…solidity…" }`

Engine: Slither static analysis + an optional free LLM reasoning pass (set `GEMINI_API_KEY` as a Space
secret to turn it on). Source: https://github.com/Yonkoo11/mantle-sentinel
