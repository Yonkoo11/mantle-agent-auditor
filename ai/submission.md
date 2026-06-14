# Sentinel — DoraHacks submission draft

> Internal draft. Review before `/submit`. Two lines must be true at submission time:
> (1) the Hunyuan/Tencent pass has run live at least once, (2) the registry source is verified on the explorer.
> If either is still pending, soften that claim (see "Honest status" at the bottom) rather than overstate it.

---

## Title
Sentinel — AI auditor for on-chain agents

## Tagline (≤ 12 words)
Audits any Mantle contract and writes a verifiable safety verdict on-chain.

## Pitch (one line)
Paste a Mantle contract; Sentinel finds the bugs and stamps a pass/fail security verdict on-chain, bound to the contract's ERC-8004 agent identity.

## The problem
The hackathon puts autonomous agents on-chain with real money and gives each an ERC-8004 identity. Nobody audits those agents or the contracts they touch. Today's options don't fit: CertiK's score is centralized and off-chain, audit firms ship PDFs, and AI auditors return a chat reply. None produce a **composable, tamper-evident, on-chain** verdict that another contract can check before trusting an agent with funds.

## What Sentinel does
1. **Reads the code** — a hybrid engine (Slither static analysis + an LLM reasoning pass on Tencent Hunyuan) finds vulnerabilities with line numbers. On the sample, it catches a reentrancy money-drain at lines 13–18.
2. **Anchors the report** — the full report is canonicalized and `keccak256`-hashed; only the hash + IPFS CID go on-chain, so the verdict is tamper-evident and falsifiable.
3. **Writes the verdict** — a pass/fail attestation lands in our `AuditAttestationRegistry` on Mantle. Any contract can call `isAttestedSafe(address)`.
4. **Binds to identity** — if the target is an ERC-8004 agent, the verdict is also written to its on-chain reputation via `ReputationRegistry.giveFeedback(...)`, so safety travels with the agent.

## Why it needs Mantle (not portable)
The product is the trust layer for *this* event's thesis. It reads the ERC-8004 identities that Mantle issues to agents, writes verdicts to a registry on Mantle, and binds those verdicts to agent reputation — four ERC-8004/Mantle primitives, all load-bearing. Remove Mantle's ERC-8004 layer and the "portable agent safety reputation" disappears.

## Live links
- Demo: https://yonkoo11.github.io/mantle-sentinel/
- Repo (open source, MIT): https://github.com/Yonkoo11/mantle-sentinel
- Registry on Mantle Sepolia: `0xbCE17E724c0Cd038622a9C4299F86Caf411C1Fae`
- Sample audited target: `0x469C46486d44eE02BB5A8d4FE341e55d13f5dF25`

## Track nomination — AI DevTools (Tencent Cloud)
Sentinel is a Mantle-specific audit assistant — exactly the track's stated target. It runs Slither plus an LLM pass on Tencent Hunyuan, and turns the result into an on-chain, queryable safety verdict. The DevTools value is concrete: a Mantle builder points Sentinel at a contract address and gets a verdict another contract can act on, not a PDF.

## Grand Champion eligibility (one paragraph, distinct)
- **Technical (30%)**: hybrid static+LLM engine, canonical-hash report anchoring, two coordinated on-chain writes (custom registry + ERC-8004 reputation) with correct nonce handling on an L2.
- **Innovation (25%)**: first auditor to bind a security verdict to an agent's ERC-8004 identity — a portable, composable safety reputation.
- **Mantle ecosystem (25%)**: four Mantle/ERC-8004 primitives load-bearing; deployed and operating on Mantle Sepolia.
- **Product completeness (20%)**: live public demo, working CLI, tests, README, MIT license.

## How to reproduce (judges)
See README — `forge test` (10 passing), run the auditor CLI against the sample, and open the demo to read the live verdict.

## Honest status (keep this accurate at submission)
- Verified live on Mantle Sepolia: Slither pass, on-chain registry write/read, ERC-8004 reputation binding (demo agent #186).
- Pending: the Tencent Hunyuan pass is coded but must be run live once before claiming it as working; explorer source-verification is pending Mantle's Blockscout API (was 503). If still pending at submit time, phrase these as "static analysis live; LLM pass via Hunyuan integrated" only after a successful call, and link the deploy tx even if the green "verified" badge isn't up yet.
