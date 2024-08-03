## Overview

This program implements a basic bigram model using the Natural Language Toolkit (NLTK). It allows users to input a text corpus to train the model and then predict the most likely next word based on the trained bigram probabilities.

## Purpose

I created this program to cement my understanding of N-gram models.

## Features

- **Download NLTK Resources**: Automatically downloads necessary NLTK resources if not already present.
- **Train Bigram Model**: Accepts a text input from the user, tokenizes it, and calculates bigram probabilities.
- **Predict Next Word**: Given a word, predicts the most likely next word based on the trained model.
- **User Interaction**: Provides options to train the model with new text or predict the next word.
- **Output**: Displays bigram probabilities in a tabular format using PrettyTable.
- **Written with Nix Flakes**: All package dependencies are installed in an isolated, version-controlled dev shell using one command.
    (Requires Nix package manager with flakes enabled)


## Installation

### Using Nix (Recommended)

1. **Set Up Your Environment with Nix**

   Make sure you have Nix and flakes enabled on your system. (See https://nixos.wiki/wiki/Flakes)
   
   The nix flake provided includes all project dependencies, including python and the required external libraries.

   

3. **Clone the Repository**

   ```bash
   git clone https://github.com/Surf-Wax/bigram-python.git
   cd bigram-python
   ```

   If you have [direnv](https://github.com/nix-community/nix-direnv) enabled on your system, you might need to run ```direnv allow``` to build the dev shell.
   Otherwise, you'll have to do it manually by running ```nix develop```

   Now you're ready to run the script!

  **NOTE**: If you're using VSCode and you're getting 'Select Interpreter' message, run `which python` in the dev shell, copy the output path. Select interpreter-> Enter interpreter path -> Paste in the output path. 

### Without Nix

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Surf-Wax/bigram-python.git
   cd bigram-python
   ```

2. **Set Up Your Environment**

   Ensure you have Python 3.x and venv installed. Create a virtual environment and install the required packages:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r pip install nltk prettytable
   ```
   
   Now you're ready to run the script!

## Usage

Run the script with the command:
```
python3 Thorpe_bigram_model.py
```

1. **Initialize Resources**: The script checks for and downloads required NLTK resources.
2. **Train the Model**: Enter a string of text when prompted to train the model. The input string should be a small corpus suitable for generating bigrams.
3. **Predict Words**: Input a word to receive predictions for the next most likely word based on the bigram model.
4. **Options**:
   - `[0] Train model on new text (corpus)`: Re-train the model with a new text input.
   - `[1] Predict word`: Predict the next word given an input word.
   - `[2] Quit`: Exit the program.

## Contact
   For any questions or comments, please reach out to thorpebryce@gmail.com.

