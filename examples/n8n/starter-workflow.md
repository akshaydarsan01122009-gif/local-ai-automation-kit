# n8n Starter Workflow

This example is the starting point for the project's n8n workflow collection.

## Goal

Create a simple automation that:

1. Starts manually.
2. Creates a small piece of input data.
3. Passes that data to a local AI service.
4. Returns the AI response.

## Why start here?

A small workflow is easier for beginners to understand and troubleshoot. More advanced agent workflows can be built on top of this pattern later.

## Local AI

The project will support local AI providers where possible. The exact provider and endpoint should be configured by the user rather than hard-coded into a shared workflow.

**Never put an API key, password, or private URL containing credentials into a workflow committed to GitHub.**

## Planned improvements

- Importable n8n workflow JSON
- Ollama example
- Structured AI output
- Error handling
- Reusable agent patterns
- Example workflows for common tasks
