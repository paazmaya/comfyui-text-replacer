import os
import re

class WordReplacer:
    """
    Replaces words based on rules loaded from a file.
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        # Determine the path to the default_rules.txt file relative to this script
        current_dir = os.path.dirname(os.path.realpath(__file__))
        default_file_path = os.path.join(current_dir, "default_rules.txt")
        
        # Try to read the file, fallback to a hardcoded string if file is missing
        default_text = "cat:dog\nblue:red"
        if os.path.exists(default_file_path):
            try:
                with open(default_file_path, "r", encoding="utf-8") as f:
                    default_text = f.read()
            except Exception as e:
                print(f"[WordReplacer] Warning: Could not read default_rules.txt: {e}")

        return {
            "required": {
                "text": ("STRING", {
                    "multiline": True, 
                    "default": "The quick brown fox jumps over the lazy cat."
                }),
                "rules": ("STRING", {
                    "multiline": True,
                    "default": default_text,
                    "tooltip": "Format: 'find:replace'. Every non-empty line must contain a colon."
                }),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("output_text",)
    FUNCTION = "replace_words"
    CATEGORY = "text/utils"
    OUTPUT_NODE = False

    def replace_words(self, text, rules):
        lines = rules.strip().split('\n')
        for line in lines:
            if not line.strip() or line.strip().startswith("#"):
                continue
                
            if ':' in line:
                find_word, replace_with = line.split(':', 1)
                find_word = find_word.strip()
                replace_with = replace_with.strip()
                
                if find_word:
                    pattern = r"\b" + re.escape(find_word) + r"\b"
                    text = re.sub(pattern, replace_with, text)
            else:
                # Log warning for invalid format lines, but don't crash
                print(f"[WordReplacer] Skipping invalid rule (missing ':'): {line}")
                
        return (text,)

NODE_CLASS_MAPPINGS = {
    "WordReplacer": WordReplacer
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "WordReplacer": "Word Replacer (Validated)"
}
