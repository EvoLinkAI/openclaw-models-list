# GPT-5.1 Thinking — via EvoLink

**Provider:** `evolink-openai`
**Model ID:** `evolink-openai/gpt-5.1-thinking`
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
          { "id": "gpt-5.1-thinking", "name": "GPT-5.1 Thinking" }
        ]
      }
    }
  }
}
```

## Set as Default

```bash
openclaw models set evolink-openai/gpt-5.1-thinking
```

## Get API Key

[Sign up at EvoLink.ai](https://evolink.ai/signup?utm_source=github&utm_medium=readme&utm_campaign=openclaw-models-list)
