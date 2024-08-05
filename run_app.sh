#!/bin/bash

# VENV Path
VENV_DIR="./amznpt"

# check if venv directory exists
if [ -d "$VENV_DIR" ]; then
  echo "Activating $VENV_DIR virtual environment..."
  source "$VENV_DIR/bin/activate"
else
  echo "$VENV_DIR virtual environment not found. Creating a new one..."
  python3 -m venv "$VENV_DIR"
  echo "Activating $VENV_DIR virtual environment..."
  source "$VENV_DIR/bin/activate"
  pip install -r requirements.txt
fi

# Run Python App
# python app.py

# Deactivate VENV
deactivate
