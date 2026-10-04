# Ollama + n8n

[Ollama](https://ollama.com/) lets you run supported AI models locally.

## Recommended setup pattern

For a local setup, keep the AI service on your own machine and let n8n send requests to it.

The exact n8n configuration depends on how n8n is installed:

- **n8n running directly on your computer:** use the local Ollama address.
- **n8n running in Docker:** the Ollama address may need to use a host or Docker-network address instead of localhost.

## Important

Do not commit:

- API keys
- passwords
- authentication tokens
- private network addresses
- personal data

## First milestone

The first working integration should:

1. Accept a text prompt.
2. Send it to a local Ollama model.
3. Return the generated response.
4. Handle a failed connection with a useful error message.

The importable n8n workflow will be added after the connection details are tested against a real n8n installation.