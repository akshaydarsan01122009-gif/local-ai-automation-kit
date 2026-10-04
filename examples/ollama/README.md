# Ollama Health Check

A tiny dependency-free Python utility that checks whether a local Ollama server is reachable.

## Requirements

- Python 3.9 or newer
- Ollama running locally

## Run

From the repository root:

    python examples/ollama/health_check.py

To use another Ollama URL:

    python examples/ollama/health_check.py --url http://localhost:11434

A successful check exits with status 0. A failed check exits with status 1.

No API key is required for a normal local Ollama installation.