# n8n Examples

This folder contains reusable n8n automation examples for Local AI Automation Kit.

## Local AI Starter

**File:** `local-ai-starter.json`

This workflow was tested with n8n and a local Ollama model. It uses:

`Manual Trigger → Edit Fields → Message a model → llama3.2:3b`

The **Edit Fields** node contains a starter prompt. The **Message a model** node reads that prompt dynamically, so you can change the prompt without editing the model node.

### Import

1. Open n8n.
2. Open a workflow.
3. Use the workflow menu to import the JSON file.
4. Open the **Message a model** node.
5. Select your own **Ollama API** credential.
6. Make sure the model `llama3.2:3b` is available in your Ollama installation.
7. Open **Edit Fields** and change the **Prompt** value if you want.
8. Execute the workflow.

### Important

The published workflow intentionally does **not** contain the original credential reference or private n8n instance metadata. Each user must select their own Ollama credential after importing.

The starter prompt is only a demonstration. Change it to your own prompt before using the workflow for real automation.

## Design rule

Examples should be safe to publish publicly. Credentials and private infrastructure details must never be committed to the repository.
