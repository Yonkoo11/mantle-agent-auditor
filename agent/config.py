"""Public configuration — addresses and endpoints only. NO secrets here.
Secrets (DEPLOYER_PRIVATE_KEY, HUNYUAN_API_KEY, etc.) are read from the environment at runtime."""

# Mantle Sepolia testnet (chain 5003)
CHAIN_ID = 5003
RPC_URL = "https://rpc.sepolia.mantle.xyz"
EXPLORER_TX = "https://sepolia.mantlescan.xyz/tx/"
EXPLORER_ADDR = "https://sepolia.mantlescan.xyz/address/"

# Our deployed registry
AUDIT_REGISTRY = "0xbCE17E724c0Cd038622a9C4299F86Caf411C1Fae"

# ERC-8004 reference deployment on Mantle Sepolia (verified live on-chain 2026-06-14)
ERC8004_IDENTITY = "0x8004A818BFB912233c491871b3d84c89A494BD9e"
ERC8004_REPUTATION = "0x8004B663056A597Dffe9eCcC1965A193B7388713"

# LLM reasoning pass — any OpenAI-compatible provider. Auto-detected by which key is set.
# Groq is the free, no-credit-card default (key: GROQ_API_KEY from https://console.groq.com).
GROQ_BASE_URL = "https://api.groq.com/openai/v1"
GROQ_MODEL = "llama-3.3-70b-versatile"
# Tencent Cloud Hunyuan — optional (sponsor-track bonus). Key: HUNYUAN_API_KEY.
HUNYUAN_BASE_URL = "https://api.hunyuan.cloud.tencent.com/v1"
HUNYUAN_MODEL = "hunyuan-turbos-latest"

# Severity ladder (string -> on-chain uint8)
SEVERITY = {"none": 0, "informational": 1, "info": 1, "low": 2, "medium": 3, "high": 4, "critical": 5}
