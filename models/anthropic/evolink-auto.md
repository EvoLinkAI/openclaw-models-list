# EvoLink Auto — Anthropic Provider

**Provider:** `evolink-anthropic`
**Model ID:** `evolink-anthropic/evolink/auto`
**API Type:** Anthropic Messages
**Base URL:** `https://direct.evolink.ai`

## What is EvoLink Auto?

Smart Model Routing — automatically selects the best model from the pool based on your request complexity, length, and type. No manual switching needed.

## OpenClaw Configuration

```json
{
  "models": {
    "providers": {
      "evolink-anthropic": {
        "api": "anthropic-messages",
        "baseUrl": "https://direct.evolink.ai",
        "apiKey": "Your EvoLink API Key",
        "models": [
          { "id": "evolink/auto", "name": "EvoLink Auto" }
        ]
      }
    }
  }
}
```

## Set as Default

```bash
openclaw models set evolink-anthropic/evolink/auto
```

## Get API Key

[Sign up at EvoLink.ai](https://evolink.ai/signup?utm_source=github&utm_medium=readme&utm_campaign=openclaw-models-list)
