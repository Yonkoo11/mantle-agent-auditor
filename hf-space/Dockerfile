# Hugging Face Space (Docker) for the Sentinel audit API.
# Self-contained: pulls the code from the public GitHub repo and runs the FastAPI auditor.
# Listens on 7860 (Hugging Face Spaces default port).
FROM python:3.11-slim

RUN apt-get update && apt-get install -y --no-install-recommends git curl && rm -rf /var/lib/apt/lists/*

# HF Spaces run as a non-root user (uid 1000) — set that up for writable home/caches.
RUN useradd -m -u 1000 user
USER user
ENV HOME=/home/user PATH=/home/user/.local/bin:$PATH
WORKDIR /home/user/app

RUN git clone --depth 1 https://github.com/Yonkoo11/mantle-sentinel.git .
RUN pip install --no-cache-dir --user -r backend/requirements.txt
RUN solc-select install 0.8.24 && solc-select use 0.8.24

EXPOSE 7860
CMD ["sh", "-c", "uvicorn backend.app:app --host 0.0.0.0 --port 7860"]
