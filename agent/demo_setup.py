"""Stand up a demo 'competing agent' owned by a SEPARATE key, so the auditor can write ERC-8004
feedback about it (the registry blocks self-feedback). The throwaway agent key is generated in
memory, funded with a little test MNT from the deployer, used once to register, then discarded —
it is never printed, logged, or written to disk. Only the resulting agentId (public) is returned."""
import os
import json

from web3 import Web3
from eth_account import Account

from config import RPC_URL, ERC8004_IDENTITY, EXPLORER_TX
from erc8004 import _IDENTITY_ABI


def main(agent_uri: str):
    w3 = Web3(Web3.HTTPProvider(RPC_URL))
    funder = Account.from_key(os.getenv("DEPLOYER_PRIVATE_KEY"))
    agent = Account.create()  # ephemeral, in-memory only

    # 1. fund the ephemeral agent with 0.05 MNT for one register tx
    nonce = w3.eth.get_transaction_count(funder.address, "pending")
    gp = w3.eth.gas_price
    fund_tx = {
        "from": funder.address, "to": agent.address, "value": w3.to_wei(0.05, "ether"),
        "nonce": nonce, "chainId": w3.eth.chain_id, "gas": 21000, "gasPrice": gp,
    }
    fh = w3.eth.send_raw_transaction(funder.sign_transaction(fund_tx).raw_transaction)
    w3.eth.wait_for_transaction_receipt(fh, timeout=180)

    # 2. register the agent from its own key
    idr = w3.eth.contract(address=Web3.to_checksum_address(ERC8004_IDENTITY), abi=_IDENTITY_ABI)
    reg = idr.functions.register(agent_uri).build_transaction({
        "from": agent.address, "nonce": w3.eth.get_transaction_count(agent.address, "pending"),
        "chainId": w3.eth.chain_id, "gas": 600000, "gasPrice": gp,
    })
    rh = w3.eth.send_raw_transaction(agent.sign_transaction(reg).raw_transaction)
    rcpt = w3.eth.wait_for_transaction_receipt(rh, timeout=180)
    import web3 as _w3
    agent_id = None
    for log in idr.events.Registered().process_receipt(rcpt, errors=_w3.logs.DISCARD):
        agent_id = log["args"]["agentId"]
        break
    th = rcpt["transactionHash"]
    ths = th.hex() if hasattr(th, "hex") else str(th)
    if not ths.startswith("0x"):
        ths = "0x" + ths
    return {"agentId": agent_id, "agentAddress": agent.address, "registerTxUrl": EXPLORER_TX + ths}


if __name__ == "__main__":
    import sys
    uri = sys.argv[1] if len(sys.argv) > 1 else "https://example-competing-agent.xyz/agent.json"
    print(json.dumps(main(uri), indent=2))
