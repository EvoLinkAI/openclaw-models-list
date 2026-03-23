# GPT-5.1 Chat — via EvoLink

**Provider:** `evolink-openai`
**Model ID:** `evolink-openai/gpt-5.1-chat`
**API Type:** OpenAI Completions
**Base URL:** `https://direct.evolink.ai/v1`

## OpenClaw Configuration

```json
{
  "models": {
    "providers": {
      "evolink-openai": {
        "api": "openai-completions",
        "baseUrl": "https://direct.evolink.ai/v1",
        "apiKey": "Your EvoLink API Key",
        "models": [
          { "id": "gpt-5.1-chat", "name": "GPT-5.1 Chat" }
        ]
      }
    }
  }
}
```

## Set as Default

```bash
openclaw models set evolink-openai/gpt-5.1-chat
```

## Get API Key

[Sign up at EvoLink.ai](https://evolink.ai/signup?utm_source=github&utm_medium=readme&utm_campaign=openclaw-models-list)
