"""Small health check for a local Ollama server."""

from __future__ import annotations

import argparse
import json
import sys
from urllib.error import URLError
from urllib.request import urlopen

def check_ollama(base_url: str) -> bool:
    """Return True when the Ollama API responds successfully."""
    url = base_url.rstrip("/") + "/api/tags"
    try:
        with urlopen(url, timeout=5) as response:
            if response.status != 200:
                return False
            json.load(response)
            return True
    except (OSError, URLError, ValueError):
        return False

def main() -> int:
    parser = argparse.ArgumentParser(description='Check local Ollama connectivity.')
    parser.add_argument('--url', default='http://localhost:11434', help='Ollama base URL')
    args = parser.parse_args()
    if check_ollama(args.url):
        print(f'Ollama is reachable at {args.url}')
        return 0
    print(f'Ollama is not reachable at {args.url}')
    return 1

if __name__ == "__main__":
    sys.exit(main())