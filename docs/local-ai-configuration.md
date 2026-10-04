# Local AI Configuration

Local AI Automation Kit is designed to work with local AI providers.

## Configuration principles

Provider settings should be configurable rather than hard-coded.

Typical settings include:

| Setting | Example | Secret? |
|---|---|---|
| Provider | Ollama | No |
| Base URL | Local service URL | Usually no |
| Model | A locally installed model | No |
| API key | Provider-specific | Yes |

## Security

Never commit real credentials to GitHub.

## Supported providers

The first documented provider is **Ollama**. Additional local providers can be documented as the project grows.