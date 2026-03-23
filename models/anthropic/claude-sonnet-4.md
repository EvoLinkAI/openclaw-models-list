# Claude Sonnet 4 — via EvoLink

**Provider:** `evolink-anthropic`
**Model ID:** `evolink-anthropic/claude-sonnet-4-20250514`
**API Type:** Anthropic Messages
**Base URL:** `https://direct.evolink.ai`

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
          { "id": "claude-sonnet-4-20250514", "name": "Claude Sonnet 4" }
        ]
      }
    }
  }
}
```

## Set as Default

```bash
openclaw models set evolink-anthropic/claude-sonnet-4-20250514
```

## Get API Key

[Sign up at EvoLink.ai](https://evolink.ai/signup?utm_source=github&utm_medium=readme&utm_campaign=openclaw-models-list)
