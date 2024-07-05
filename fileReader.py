import fitz  # PyMuPDF
from PyPDF2 import PdfReader
from docx import Document 
import os
from splitter import text_to_doc_splitter

def extract_text(file_path):
    _, file_extension = os.path.splitext(file_path)

    if file_extension.lower() == '.pdf':
        return extract_text_from_pdf(file_path)
    elif file_extension.lower() == '.docx':
        return extract_text_from_docx(file_path)
    else:
        raise ValueError('Unsupported file type: {}'.format(file_extension))

def extract_text_from_pdf(file_path):
    # Using PyPDF2 to extract text from PDF
    pdf_reader = PdfReader(file_path)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def extract_text_from_docx(file_path):
    document = Document(file_path)
    text = "\n".join([para.text for para in document.paragraphs])
    return text

def load_document(file_path):
    text = extract_text(file_path)
    document = text_to_doc_splitter(text)
    return document
