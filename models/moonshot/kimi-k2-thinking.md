# Kimi K2 Thinking — via EvoLink

**Provider:** `evolink-openai`
**Model ID:** `evolink-openai/kimi-k2-thinking`
**API Type:** OpenAI Completions (Moonshot Kimi)
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
          { "id": "kimi-k2-thinking", "name": "Kimi K2 Thinking" }
        ]
      }
    }
  }
}
```

## Set as Default

```bash
openclaw models set evolink-openai/kimi-k2-thinking
```

## Get API Key

[Sign up at EvoLink.ai](https://evolink.ai/signup?utm_source=github&utm_medium=readme&utm_campaign=openclaw-models-list)
