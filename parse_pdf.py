print("script started")

import fitz
import re
import json
from pathlib import Path

print("script started")

PDF_PATH = "data/Modulhandbuch_MMI_V1-0.pdf"
OUTPUT_PATH ="data/modules.json"

doc = fitz.open(PDF_PATH)
all_text = ""
for page in doc:
    all_text += page.get_text()

pattern = re.compile(r"(MMI \d{2}(?:\.\d{2})?: .*?)(?=MMI \d{2}(?:\.\d{2})?: |\Z)", re.DOTALL)
matches = pattern.findall(all_text)

modules = []

for raw in matches:
    #extract module ID and title
    header_match = re.match(r"(MMI \d{2}(?:\.\d{2})?): (.*)", raw)
    if not header_match:
        continue
    module_id = header_match.group(1).strip()
    title = header_match.group(2).split("\n")[0].strip()

    #save the chunk
    modules.append({
        "module_id": module_id,
        "title": title,
        "content": raw.strip()
    })

Path("data").mkdir(exist_ok=True)
with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    json.dump(modules, f, indent=2, ensure_ascii=False)

print(f"sucessfully extracted and saved {len(modules)} modules to {OUTPUT_PATH}")