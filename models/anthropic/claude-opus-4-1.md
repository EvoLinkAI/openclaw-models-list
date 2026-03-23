# Claude Opus 4.1

**Provider:** `anthropic`
**Model ID:** `anthropic/claude-opus-4-1-20250805`
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
          { "id": "claude-opus-4-1-20250805", "name": "Claude Opus 4.1" }
        ]
      }
    }
  }
}
```

## Set as Default

```bash
openclaw models set anthropic/claude-opus-4-1-20250805
```
