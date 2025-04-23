#!/bin/bash

echo "===== PDF Finder Installation ====="
echo "Setting up environment for PDF Finder with OCR capabilities"

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is required but not installed."
    echo "Please install Python 3 before continuing."
    exit 1
fi

# Check if pip is installed
if ! command -v pip &> /dev/null; then
    echo "Error: pip is required but not installed."
    echo "Please install pip before continuing."
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install Python dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

# Check for Homebrew (macOS)
if [[ "$OSTYPE" == "darwin"* ]]; then
    if ! command -v brew &> /dev/null; then
        echo "Homebrew not found. Please install Homebrew first."
        echo "Visit https://brew.sh for installation instructions."
        exit 1
    fi
    
    echo "Installing Tesseract OCR and Poppler via Homebrew..."
    brew install tesseract poppler
    
# Check for apt-get (Debian/Ubuntu)
elif command -v apt-get &> /dev/null; then
    echo "Installing Tesseract OCR and Poppler via apt..."
    sudo apt-get update
    sudo apt-get install -y tesseract-ocr poppler-utils
    
# Check for other package managers as needed
else
    echo "Warning: Could not detect package manager to install Tesseract and Poppler."
    echo "Please install Tesseract OCR and Poppler manually according to your OS."
    echo "See README.md for instructions."
fi

# Create a convenient run script
cat > run.sh << 'EOL'
#!/bin/bash

# Activate the virtual environment
source venv/bin/activate

# Run the script with any arguments passed to this shell script
python pdf_finder.py "$@"
EOL

chmod +x run.sh

# Create pdf directory if it doesn't exist
if [ ! -d "pdf" ]; then
    mkdir -p pdf
    echo "Created 'pdf' directory for your PDF files"
fi

echo
echo "===== Installation Complete ====="
echo "To use PDF Finder:"
echo "1. Place your PDF files in the 'pdf' directory"
echo "2. Run: ./run.sh \"your search term\""
echo 