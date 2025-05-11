
import os
import pytesseract
from pdf2image import convert_from_path
import json
from pathlib import Path

# --------------- CONFIG ------------------
INPUT_PDF = "sample/input.pdf"
OUTPUT_JSON = "sample/output.json"
TESSERACT_CMD = "tesseract"  # Change this path if needed, e.g., "C:/Program Files/Tesseract-OCR/tesseract.exe"
# -----------------------------------------

# Ensure Tesseract command is registered (for Windows systems)
pytesseract.pytesseract.tesseract_cmd = TESSERACT_CMD

# Convert PDF pages to images
print(f"Converting PDF to images: {INPUT_PDF}")
pages = convert_from_path(INPUT_PDF)

extracted_text = []

for i, page in enumerate(pages):
    text = pytesseract.image_to_string(page)
    extracted_text.append({
        "page": i + 1,
        "text": text.strip()
    })
    print(f"Processed page {i + 1}")

# Save extracted text to JSON
with open(OUTPUT_JSON, "w", encoding="utf-8") as out_file:
    json.dump(extracted_text, out_file, indent=4)

print(f"Text extraction completed. Output saved to {OUTPUT_JSON}")
