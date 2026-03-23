# Doubao Seed 2.0 Code — via EvoLink

**Provider:** `evolink-openai`
**Model ID:** `evolink-openai/doubao-seed-2.0-code`
**API Type:** OpenAI Completions (ByteDance Doubao)
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
          { "id": "doubao-seed-2.0-code", "name": "Doubao Seed 2.0 Code" }
        ]
      }
    }
  }
}
```

## Set as Default

```bash
openclaw models set evolink-openai/doubao-seed-2.0-code
```

## Get API Key

[Sign up at EvoLink.ai](https://evolink.ai/signup?utm_source=github&utm_medium=readme&utm_campaign=openclaw-models-list)
