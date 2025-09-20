import os
import yaml
from typing import Dict

languages: Dict[str, dict] = {}
languages_present: Dict[str, str] = {}

# Load English first as the fallback
try:
    with open("./strings/langs/en.yml", encoding="utf8") as f:
        languages["en"] = yaml.safe_load(f)
        languages_present["en"] = languages["en"].get("name", "English")
except FileNotFoundError:
    print("Error: 'en.yml' language file not found in ./strings/langs/")
    exit()

# Load other language files
for filename in os.listdir("./strings/langs/"):
    if not filename.endswith(".yml") or filename == "en.yml":
        continue

    lang_code = filename[:-4]  # Remove .yml extension
    try:
        with open(f"./strings/langs/{filename}", encoding="utf8") as f:
            lang_data = yaml.safe_load(f)

        # Fill missing keys from English
        for key in languages["en"]:
            if key not in lang_data:
                lang_data[key] = languages["en"][key]

        languages[lang_code] = lang_data
        languages_present[lang_code] = lang_data.get("name", lang_code)
    except Exception as e:
        print(f"Error loading language file '{filename}': {e}")
        continue

def get_string(lang_code: str):
    """
    Returns the language dictionary for the given lang_code.
    Falls back to English if lang_code not found.
    """
    return languages.get(lang_code, languages["en"])
