# Design Research Brief — Sentinel

## Product category
On-chain security/attestation tool with a data-display surface (read a verdict from chain). Dev-tool tone.

## Comparables studied
- **EAS (attest.org)** — direct adjacent (attestations). The attestation object is the hero: clear
  key-value fields, schema, hash. Calm, minimal. STEAL: make the verdict a tangible object with crisp
  key-value rows (hash, identity, severity). AVOID: their generic explorer chrome.
- **Linear** — dark dashboard craft. Restrained palette, one accent, superb tight typography, fast
  micro-motion (~150ms). STEAL: tight letter-spacing on display type, hairline tinted borders, calm
  surface with a single accent, GPU-only motion. AVOID: nothing — taste benchmark.
- **Etherscan / Blockscout** — on-chain data display. STEAL: monospace addresses/hashes with
  tabular-nums, explicit tx links, key-value clarity. AVOID: their cluttered density and dead-flat bg.
- **Vercel** — dev-tool landing. STEAL: high-contrast bold type, generous negative space, crisp edges.

## Common patterns (table stakes)
- Dark surface, single accent, monospace for on-chain data, clear key-value verdict display, explicit
  links to the chain (proof, not claims).

## Differentiation (our signature)
- **The verdict as a credential object.** Nobody renders a security verdict as an on-chain, identity-bound
  object. Make the verdict card the hero — a "passport stamp" for an agent: PASS/FAIL, severity, the
  ERC-8004 identity it's bound to, the report hash you can re-check. That object is the whole product.

## Constraints
- Must stay functional: reads live from Mantle via RPC; keep all element IDs app.js depends on.
- Offline-safe for demo recording: no external font/script CDNs (system + vendored ethers only).
- body min 14px; tabular-nums on all data; one accent (Mantle mint), brand-justified.

## Anti-patterns to avoid (style config + slop gates)
- AI-slop purple-blue/teal-coral gradients; gradient text; rounded-everything; identical card grids;
  self-certifying badges; generic "Get Started" CTAs; flat dead background.

## Stolen elements (adopt + adapt)
- From EAS: verdict-as-object key-value rows.
- From Linear: tight display tracking, hairline borders, 150ms GPU motion, calm one-accent dark surface.
- From Etherscan: mono + tabular-nums for hash/address, explicit chain links.
- From Vercel: bold type + negative space.
