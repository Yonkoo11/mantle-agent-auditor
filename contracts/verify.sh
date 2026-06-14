#!/usr/bin/env bash
# Verify AuditAttestationRegistry source on the Mantle Sepolia explorer.
# Blockscout's verify API (explorer.sepolia.mantle.xyz) was returning 503 during the build —
# rerun this when it's back up. No API key needed for Blockscout.
set -e
ADDR=0xbCE17E724c0Cd038622a9C4299F86Caf411C1Fae
forge verify-contract "$ADDR" src/AuditAttestationRegistry.sol:AuditAttestationRegistry \
  --rpc-url https://rpc.sepolia.mantle.xyz \
  --verifier blockscout \
  --verifier-url https://explorer.sepolia.mantle.xyz/api/ \
  --compiler-version 0.8.24 \
  --num-of-optimizations 200 \
  --evm-version cancun
