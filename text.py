from docling.document_converter import DocumentConverter
from pathlib import Path

source = "MER April 2021_0.pdf"



converter = DocumentConverter()

result = converter.convert(source)

output_dir = Path("MER-Text")

output_dir.mkdir(parents=True, exist_ok=True)  

text_content = result.document.export_to_text()

text_filename = output_dir / "Extracted_Text.txt"

with open(text_filename, "w", encoding="utf-8") as f:
    f.write(text_content)

print(f"Extracted text saved in: {text_filename}")
