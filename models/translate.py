import os
from pathlib import Path

# Languages
langs = ["de", "es", "fr", "ja", "ko", "ru", "tr", "zh-CN", "zh-TW"]

for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".md"):
            path = Path(root) / file
            # Skip if already translated (if I organize by lang)
            # Actually, I should probably store them as <file>.<lang>.md or similar if I don't want to pollute with folders.
            # But the task says "translate all content inside the /models directory (individual markdown files for each model) into the 9 target languages".
            # The structure for READMEs is already flat with suffixes.
            # I will use the same pattern: <name>.<lang>.md for each model file.
            
            for lang in langs:
                new_file = path.parent / f"{path.stem}.{lang}.md"
                # Call translate tool (I don't have a direct translate tool, I have Gemini model to do it)
                # I will simulate this or use a prompt.
                # Actually, I need to use the LLM to translate the content.
                # Since I am an agent, I can read the file content and rewrite it.
