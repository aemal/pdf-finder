#!/usr/bin/env python3

import os
import re
import sys
import PyPDF2
import pdfplumber
import pytesseract
from pdf2image import convert_from_path
import tempfile

def find_text_in_pdfs(folder_path, search_term):
    """
    Search for a term in all PDF files in the specified folder using multiple methods:
    1. Standard text extraction with PyPDF2
    2. Advanced text extraction with pdfplumber
    3. OCR using Tesseract
    Print the filenames and page numbers where the term is found.
    """
    # Check if folder exists
    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' does not exist.")
        return
    
    # Check if folder is empty
    pdf_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.pdf')]
    if not pdf_files:
        print(f"No PDF files found in '{folder_path}'.")
        return
    
    print(f"Searching for '{search_term}' in {len(pdf_files)} PDF files...")
    found_results = False
    
    for pdf_file in pdf_files:
        file_path = os.path.join(folder_path, pdf_file)
        
        # Method 1: Try using PyPDF2 first
        try:
            # Open the PDF with PyPDF2
            with open(file_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                
                # Search in each page
                for page_num in range(len(reader.pages)):
                    # Get text from the page
                    page = reader.pages[page_num]
                    text = page.extract_text()
                    
                    # Search for the term (case-insensitive)
                    if text and re.search(re.escape(search_term), text, re.IGNORECASE):
                        if not found_results:
                            found_results = True
                        print(f"Found in '{pdf_file}' - Page {page_num + 1} (PyPDF2)")
        except Exception as e:
            print(f"Error processing '{pdf_file}' with PyPDF2: {e}")
            
        # Method 2: Try using pdfplumber for better extraction
        try:
            with pdfplumber.open(file_path) as pdf:
                for page_num, page in enumerate(pdf.pages):
                    text = page.extract_text()
                    if text and re.search(re.escape(search_term), text, re.IGNORECASE):
                        if not found_results:
                            found_results = True
                        print(f"Found in '{pdf_file}' - Page {page_num + 1} (pdfplumber)")
                        
                    # Try extracting table data which might contain the number
                    tables = page.extract_tables()
                    for table in tables:
                        for row in table:
                            for cell in row:
                                if cell and re.search(re.escape(search_term), str(cell), re.IGNORECASE):
                                    if not found_results:
                                        found_results = True
                                    print(f"Found in '{pdf_file}' - Page {page_num + 1} (in table)")
        except Exception as e:
            print(f"Error processing '{pdf_file}' with pdfplumber: {e}")
        
        # Method 3: Try using OCR with Tesseract
        try:
            print(f"Trying OCR on '{pdf_file}'. This may take a while...")
            # Convert PDF to images
            with tempfile.TemporaryDirectory() as temp_dir:
                images = convert_from_path(file_path)
                
                # Process each page image with OCR
                for i, image in enumerate(images):
                    # Apply OCR to get text
                    ocr_text = pytesseract.image_to_string(image)
                    
                    # Search for the term
                    if ocr_text and re.search(re.escape(search_term), ocr_text, re.IGNORECASE):
                        if not found_results:
                            found_results = True
                        print(f"Found in '{pdf_file}' - Page {i + 1} (OCR)")
                        
                        # Print context around the match for verification
                        lines = ocr_text.split('\n')
                        for line_num, line in enumerate(lines):
                            if re.search(re.escape(search_term), line, re.IGNORECASE):
                                print(f"  Context: ...{line.strip()}...")
        except Exception as e:
            print(f"Error processing '{pdf_file}' with OCR: {e}")
    
    if not found_results:
        print(f"No matches found for '{search_term}'.")
        print("Note: If you can see the text in Preview but OCR isn't finding it,")
        print("you may need to check Tesseract installation or try a different approach.")

def main():
    if len(sys.argv) != 2:
        print("Usage: python pdf_finder.py <search_term>")
        return
    
    search_term = sys.argv[1]
    folder_path = "pdf"
    
    find_text_in_pdfs(folder_path, search_term)

if __name__ == "__main__":
    main() 