
# 🧠 Local Text Extraction from PDF using Tesseract OCR

This offline Python project extracts text from PDF documents using **Tesseract OCR** and **pdf2image**, without relying on any cloud API like IBM Watsonx.

---

## 📦 Features

- Convert PDFs to images
- Use Tesseract to extract text from each page
- Save output as a structured JSON file
- Fully local — no cloud credentials required

---

## 📂 Folder Structure

```
.
├── text_extraction_local.py       # Main script
├── requirements_local.txt         # Local-only dependencies
├── README.md                      # Project documentation
└── sample/                        # Input/output folder
    ├── input.pdf
    └── output.json
```

---

## 🔧 Installation & Setup

1. **Install system tools**
   - Install [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
   - Install `poppler` (required by `pdf2image`)
     - Windows: [Poppler for Windows](http://blog.alivate.com.au/poppler-windows/)
     - macOS: `brew install poppler`
     - Linux: `sudo apt install poppler-utils`

2. **Clone the repo & install dependencies**
   ```bash
   git clone https://github.com/yourusername/Local-PDF-Text-Extractor.git
   cd Local-PDF-Text-Extractor
   pip install -r requirements_local.txt
   ```

3. **Run the script**
   ```bash
   python text_extraction_local.py
   ```

---

## 📈 Output Format (JSON)

Each PDF page is processed into:
```json
[
  {
    "page": 1,
    "text": "Extracted text from page 1..."
  },
  ...
]
```

---

## 🔒 License

MIT License — Free to use and modify.
