# PDF Finder with OCR

A tool to search for text in PDF files using multiple methods, including OCR (Optical Character Recognition).

## Purpose

This project was created to solve a common problem: searching through dozens of PDF files quickly and efficiently. For example, when you need to find a specific transaction in your credit card history across multiple statements:

1. Download all your PDF statements from your bank
2. Place them in the `/pdf` folder
3. Run `./run.sh "search term"` to locate the exact page and file where the term appears

I personally use this tool all the time to search through financial documents, receipts, and statements, and thought it would be valuable to share with the world.

## Features

- Basic text extraction using PyPDF2
- Advanced text extraction with pdfplumber (better at handling complex layouts)
- OCR-based text extraction using Tesseract (can read text from images/scans)
- Table data extraction for structured content

## Requirements

- Python 3.6+
- Tesseract OCR engine
- poppler (for pdf2image)

## Quick Installation

The easiest way to install is using the provided installation script:

```bash
# Clone the repository
git clone https://github.com/yourusername/pdf-finder.git
cd pdf-finder

# Run the installation script
./install.sh
```

The installation script will:
1. Create a Python virtual environment
2. Install all required Python dependencies
3. Install Tesseract OCR and Poppler if on a supported system (macOS or Debian/Ubuntu)
4. Create a convenient run script for daily use

## Manual Installation

If you prefer to install manually:

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - macOS/Linux: `source venv/bin/activate`
   - Windows: `venv\Scripts\activate`
4. Install Python dependencies: `pip install -r requirements.txt`
5. Install external dependencies:

   ### macOS
   ```
   brew install tesseract poppler
   ```

   ### Linux (Ubuntu/Debian)
   ```
   apt-get install tesseract-ocr poppler-utils
   ```

   ### Windows
   - Download and install Tesseract from https://github.com/UB-Mannheim/tesseract/wiki
   - Download and install poppler from http://blog.alivate.com.au/poppler-windows/
   - Add both to your PATH

## Usage

1. Place your PDF files in the `pdf` directory
2. Run the script with your search term:

   ```bash
   # Quick usage
   ./run.sh "your search term"
   
   # Or with manual activation
   source venv/bin/activate
   python pdf_finder.py "your search term"
   ```

3. The script will search using all three methods (basic extraction, advanced extraction, and OCR) and display where your term was found

## Example Use Cases

- Finding specific transactions in bank or credit card statements
- Searching through tax documents for specific amounts or references
- Locating mentions of certain terms across multiple research papers
- Finding information in scanned documents that aren't text-searchable

## How It Works

The tool uses three different approaches to find text in PDFs:

1. **PyPDF2**: Fast basic text extraction
2. **pdfplumber**: More advanced extraction that handles tables and complex layouts
3. **Tesseract OCR**: Converts PDF pages to images and applies OCR to read text from scanned documents or images

This multi-method approach helps find text that might be missed by any single method alone.

## Troubleshooting

If macOS Preview can find text that this tool cannot, it might be because:
1. The PDF contains text in images that requires better OCR
2. The text is using a special font or encoding
3. The PDF has complex formatting or structure

If Tesseract OCR is installed correctly but still not finding text, you might need to:
- Improve the image quality before OCR
- Try different Tesseract parameters or language settings
- Use a cloud-based OCR service for better results

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Created by [Aemal Sayer](https://AemalSayer.com) 