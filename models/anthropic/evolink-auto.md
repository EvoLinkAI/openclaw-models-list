# EvoLink Auto

**Provider:** `anthropic`
**Model ID:** `anthropic/evolink/auto`
**API Type:** anthropic-messages
**Base URL:** `https://direct.evolink.ai`

## OpenClaw Configuration

```json
{
  "models": {
    "providers": {
      "anthropic": {
        "api": "anthropic-messages",
        "baseUrl": "https://direct.evolink.ai",
        "apiKey": "YOUR_API_KEY",
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
openclaw models set anthropic/evolink/auto
```
