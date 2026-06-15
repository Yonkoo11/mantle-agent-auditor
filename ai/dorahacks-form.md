# DoraHacks BUIDL form — copy/paste source (Sentinel)

Copy each field straight from here. Written in plain prose, no AI tells.
NOTE: only the **Profile** tab was confirmed from a screenshot. Details / Team / Contact / Submission
are filled from the standard DoraHacks form — confirm the field labels against your tabs and tell me
if any differ.

================================================================
## TAB 1 — PROFILE  (confirmed from screenshot)
================================================================

### Vision  (Describe the problem which this project solves)  [MAX 256 CHARS — this is 249]
Autonomous agents move real money on Mantle, each with an on-chain identity, but no one checks if their contracts are safe. Audits are PDFs; scores live off-chain. Sentinel writes a pass/fail verdict on-chain, bound to the agent's ERC-8004 identity.

(Longer version for any field WITHOUT a limit, e.g. the Details description:)
Autonomous agents now move real money on Mantle, and every agent gets an on-chain identity. Nobody checks whether the contracts behind them are safe. Audit firms hand back PDFs. Security scores sit on websites a smart contract can't read. There is no way for one contract to ask, on-chain, whether another agent has been audited and passed. Sentinel answers that. It audits any contract, writes a pass or fail verdict to Mantle, and ties it to the agent's ERC-8004 identity, so anyone can check it and any contract can act on it.

### Category
Crypto / Web3
(If you'd rather lead with the AI angle, AI / Robotics also fits. Crypto / Web3 is the stronger primary
because the core of the product is the on-chain verdict registry.)

### Is this BUIDL an AI Agent?
Yes  (toggle ON)
Reason: Sentinel registers its own ERC-8004 agent identity and runs an autonomous audit pipeline that
reads a contract, reasons about it with an LLM, and writes its verdict on-chain without a human in the loop.

### Links
GitHub:           https://github.com/Yonkoo11/mantle-sentinel
Project website:  https://yonkoo11.github.io/mantle-sentinel/

================================================================
## TAB 2 — DETAILS   (standard form — confirm labels)
================================================================

### Short tagline / intro
An AI auditor that grades any contract and writes the verdict on-chain, bound to the agent's ERC-8004 identity.

### Full description
Sentinel is an AI auditor for on-chain agents. You give it a contract, it finds the bugs, and it writes a pass or fail security verdict onto Mantle. The verdict is bound to the contract's ERC-8004 agent identity, so an agent's safety reputation lives on-chain and travels with it.

How it works:

1. Read the code. A hybrid engine runs Slither for static analysis and Google Gemini for the logic bugs static tools miss. The two passes are merged, so an issue both engines flag is marked as confirmed. On a sample vault it catches a reentrancy money-drain at the exact lines; on a tx.origin contract the AI pass adds a critical "owner can drain all funds" that the static tool phrased only as a warning.

2. Anchor the report. The full report is reduced to a single keccak256 hash. Only the hash and an IPFS pointer go on-chain, so the verdict is cheap to store and can't be altered after the fact. Anyone can re-run the report and confirm the hash matches.

3. Write the verdict. A pass or fail attestation is written to the AuditAttestationRegistry contract on Mantle Sepolia. Any other contract can call isAttestedSafe(address) and gate its own logic on the result.

4. Bind to identity. If the audited contract is a registered ERC-8004 agent, the verdict is also written to its on-chain reputation through the ReputationRegistry. The safety record follows the agent's identity instead of a link that can rot.

What's live right now:
- Registry contract deployed and running on Mantle Sepolia: 0xbCE17E724c0Cd038622a9C4299F86Caf411C1Fae
- A web app that reads verdicts straight from the chain, plus a hosted backend that audits any pasted contract on demand.
- A real verdict bound to ERC-8004 agent #186, readable back on-chain with getSummary.
- Three contracts already graded in the public registry: one passing at grade A, two failing at grade D.

Why it needs Mantle:
The product is the trust layer for this event's own thesis. It reads the ERC-8004 identities Mantle issues to agents, writes verdicts to a Mantle contract, and binds those verdicts to agent reputation. Remove Mantle's ERC-8004 layer and the idea of a portable, on-chain agent safety reputation has nowhere to live.

### Tech stack / Built with
Mantle Sepolia, Solidity, Foundry (10 passing tests), Slither, Google Gemini, Python, FastAPI, ethers.js, ERC-8004 Identity and Reputation registries, Hugging Face Spaces, GitHub Pages.

### Logo / cover image
Use the shield-check mark in mint on near-black. (If you generate the logo, upload it here.)

================================================================
## TAB 3 — TEAM   (standard form — confirm labels)
================================================================
Solo builder.
Name / handle: [your name or handle]
Role: builder. Contracts, audit engine, and frontend.
(Add GitHub: Yonkoo11 if it asks for a profile.)

================================================================
## TAB 4 — CONTACT   (standard form — confirm labels)
================================================================
Email:     [your email]
Telegram:  [your handle, if asked]
X / Twitter: [your handle, if asked]

================================================================
## TAB 5 — SUBMISSION   (standard form — confirm labels)
================================================================

### Hackathon / Track
Mantle Turing Test Hackathon 2026 (AI Awakening).
Track: AI DevTools (Tencent Cloud). Also nominating for Grand Champion.

### Demo video
[paste the YouTube unlisted link after you upload video/mantle-sentinel-demo.mp4]

### What was built during the hackathon
Everything in the repo was built for this event: the on-chain attestation registry and its tests, the
hybrid Slither + Gemini audit engine, the canonical-hash report anchoring, the ERC-8004 identity and
reputation writes, the hosted audit-any-contract backend, the web app, and the live verdict registry.

### Deployed contract address (Mantle Sepolia, chain 5003)
AuditAttestationRegistry: 0xbCE17E724c0Cd038622a9C4299F86Caf411C1Fae
Sample audited target:    0x469C46486d44eE02BB5A8d4FE341e55d13f5dF25

### Live demo
https://yonkoo11.github.io/mantle-sentinel/

### Repository
https://github.com/Yonkoo11/mantle-sentinel
