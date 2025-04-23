#!/bin/bash

# Activate the virtual environment
source venv/bin/activate

# Run the script with any arguments passed to this shell script
python pdf_finder.py "$@"
