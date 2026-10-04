# Local AI Automation Kit

Open-source toolkit for building practical local AI automation, agents, and n8n workflows.

> **Status:** Early development

## What is this?

A beginner-friendly collection of tools, examples, workflows, and documentation for connecting local AI models with automation systems.

The goal is simple: make useful AI automation understandable and reproducible without requiring advanced programming knowledge.

## Current examples

### n8n + Ollama

The project currently includes two working n8n examples:

- **Local AI Starter** — sends a reusable prompt from an n8n field to a local Ollama model.
- **Local AI Health Check** — checks the local Ollama API and reports the available models.

See `examples/n8n/` for the workflows and import instructions.

## Quick start

The project is designed around local AI tools such as Ollama and automation tools such as n8n.

For a beginner-friendly setup, start with:

1. Install and verify Ollama.
2. Make sure a local model is available.
3. Install or open n8n.
4. Configure n8n to access your local Ollama server.
5. Import the **Local AI Starter** workflow.
6. Run it and change the prompt in the **Edit Fields** node.
7. Use the **Local AI Health Check** workflow when you want to verify that Ollama is responding.

Detailed setup documentation is available in `docs/`.

## Planned features

- 🤖 Local AI agent examples
- 🔄 More n8n workflow templates
- 🐳 Docker-based setup examples
- 🧩 Reusable automation components
- 📚 Beginner-friendly documentation
- 🧪 Automated checks with GitHub Actions

## Who is this for?

- People learning local AI
- n8n users
- Developers experimenting with AI agents
- Self-hosting enthusiasts
- Open-source contributors

## Project principles

**Useful over flashy.** Examples should solve real problems.

**Simple over complicated.** A beginner should be able to understand the basic workflow.

**Reproducible over mysterious.** Setup steps and configuration should be documented.

**Open by default.** The project is intended to be useful to the wider open-source community.

## Contributing

Contributions are welcome. See `CONTRIBUTING.md`.

## Security

Never commit API keys, passwords, tokens, or other secrets. See `SECURITY.md`.

## License

MIT License. See `LICENSE`.
