import docx2txt
import fitz  # PyMuPDF

def extract_text_from_docx(path):
    return docx2txt.process(path)

def extract_text_from_pdf(path):
    text = ""
    doc = fitz.open(path)
    for page in doc:
        text += page.get_text()
    return text
