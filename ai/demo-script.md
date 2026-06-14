# Sentinel — demo video script (target ≤ 2:00)

Structure: Problem → Solution → Demo → Team. Screen-record the real product; cursor visible. No music,
no slop words. Captions on (judges may scrub muted). Thumbnail = the verdict screen, not a logo.

Two takes possible:
- **A (recommended):** record once the Tencent Hunyuan pass is live, so you can show the hybrid engine.
- **B (fallback):** record now with Slither-only and say so honestly ("LLM pass via Hunyuan is wired in;
  this run shows the static layer"). Better an honest demo than a delayed one.

---

## 0:00–0:15 — Problem
SAY: "This hackathon puts AI agents on-chain with real money, each with an ERC-8004 identity. But nobody
audits them. CertiK's score lives off-chain, audit firms ship PDFs — none of it is something a contract
can actually check before trusting an agent."
SHOW: the live demo page header (Sentinel) + the ERC-8004 line.

## 0:15–0:35 — Solution
SAY: "Sentinel is an AI auditor for on-chain agents. Paste a Mantle contract, it finds the bugs, and it
writes a pass/fail safety verdict on-chain — bound to the agent's ERC-8004 identity, so the verdict
travels with the agent."
SHOW: the four "How it works" steps on the page.

## 0:35–1:25 — Demo (the golden path, real)
1. In a terminal: run the auditor on the sample contract.
   SHOW: the CLI output — VERDICT: FAIL, the reentrancy finding at lines 13–18, the report hash.
   SAY: "It read the contract, found a real reentrancy money-drain at these exact lines, and decided FAIL."
2. SHOW: the registry tx + the ERC-8004 reputation tx printed by the CLI (open one on the explorer).
   SAY: "It wrote the verdict to Mantle, and bound it to the agent's ERC-8004 reputation."
3. SWITCH to the live demo page → paste the sample address → click Check verdict.
   SHOW: the verdict card — FAIL, findings 3, severity high, ERC-8004 agent #186, report hash, tx link.
   SAY: "Anyone can read that verdict straight from Mantle — no backend, no login. Another contract can
   call isAttestedSafe and act on it."

## 1:25–1:45 — Why it's Mantle-native
SAY: "This only works here. It reads the ERC-8004 identities Mantle issues, writes to a registry on
Mantle, and binds verdicts to agent reputation — four primitives, all load-bearing."
SHOW: the registry on the explorer (or the deploy tx if 'verified' badge isn't up yet).

## 1:45–2:00 — Team + close
SAY: "I build smart-contract security tooling. Sentinel is the safety layer the agent economy is missing.
It's open source, MIT, live on Mantle Sepolia today."
SHOW: the repo + the live demo URL on screen.

---

## Pre-record checklist
- [ ] Terminal font large enough to read; clear the scrollback first.
- [ ] Demo page open in a fresh browser tab (incognito) so it works without your wallet pre-installed.
- [ ] Sample address copied: 0x469C46486d44eE02BB5A8d4FE341e55d13f5dF25
- [ ] One explorer tab pre-loaded to a verdict tx so it loads instantly on camera.
- [ ] If recording take B, the "Hunyuan wired in, this run shows the static layer" line is in the script.
- [ ] Keep it under 2:00. Cut the Mantle-native section first if over.
