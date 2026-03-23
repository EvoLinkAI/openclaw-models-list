# Claude Opus 4.6

**Provider:** `anthropic`
**Model ID:** `anthropic/claude-opus-4-6`
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
          { "id": "claude-opus-4-6", "name": "Claude Opus 4.6" }
        ]
      }
    }
  }
}
```

## Set as Default

```bash
openclaw models set anthropic/claude-opus-4-6
```
