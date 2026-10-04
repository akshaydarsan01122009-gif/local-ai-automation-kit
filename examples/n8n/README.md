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

## Local AI Health Check

**File:** `local-ai-health-check.json`

This workflow checks whether a local Ollama server is responding and lists the models available through its local API.

It uses:

`Manual Trigger → HTTP Request → Code in JavaScript`

The HTTP Request calls:

`http://127.0.0.1:11434/api/tags`

The JavaScript step converts the API response into a small status result and lists the available model names.

### Import

1. Import `local-ai-health-check.json` into n8n.
2. Make sure Ollama is running locally.
3. Execute the workflow.
4. Check the final status and model list.

### Important

The published workflows intentionally do **not** contain private credential references or n8n instance metadata. The health-check example uses Ollama's local API directly and does not require an n8n credential.

The examples assume Ollama is listening on `127.0.0.1:11434`. If your Ollama server uses a different address or port, update the HTTP Request node.

## Design rule

Examples should be safe to publish publicly. Credentials and private infrastructure details must never be committed to the repository.
