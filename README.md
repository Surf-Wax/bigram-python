# Natural Language Processing with NLTK - Query Experimentation

## Overview

The NLTK Query Experimentation project provides an interactive framework for exploring and analyzing text corpora using the Natural Language Toolkit (NLTK). This project allows users to perform various text processing tasks, such as tokenization, word frequency analysis, and concordance generation, using both built-in and user-specified corpora.

## Features

- **Corpus Initialization**: Load and initialize text corpora from both local directories and NLTK's built-in datasets.
- **Tokenization**: Break down raw text into tokens for further analysis.
- **Text Analysis**: Perform common text analysis tasks, including:
  - Calculating the length of the corpus.
  - Counting the number of tokens.
  - Determining vocabulary size.
  - Searching for word occurrences.
  - Generating concordances.
  - Finding word similarities.
  - Displaying word index positions.
  - Compiling and displaying vocabulary frequencies.

## Installation

### Using Nix (Recommended)

1. **Set Up Your Environment with Nix**

   Make sure you have Nix and flakes enabled on your system. (See https://nixos.wiki/wiki/Flakes)
   
   The nix flake provided includes all project dependencies, including python and the required external libraries.

   

3. **Clone the Repository**

   ```bash
   git clone https://github.com/Surf-Wax/Natural-Language-Processing.git
   cd Natural-Language-Processing
   ```

   If you have [direnv](https://github.com/nix-community/nix-direnv) enabled on your system, you might need to run ```direnv allow``` to build the dev shell.
   Otherwise, you'll have to do it manually by running ```nix develop```

   Now you're ready to run the script!

  **NOTE**: If you're using VSCode and you're getting 'Select Interpreter' message, run `which python` in the dev shell, copy the output path. Select interpreter-> Enter interpreter path -> Paste the output path. 

### Without Nix

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Surf-Wax/Natural-Language-Processing.git
   cd Natural-Language-Processing
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
1. **Run the Script**

   NOTE: The script will download the necessary NLTK resources into a folder called '**nltk_data**' in your current working directory.

   Execute the main script to start the NLTK Query Experimentation:

   ```bash
   python3 Thorpe_NLTK.py
   ```

2. **Interact with the Application**
   Follow the on-screen prompts to select options and provide paths to corpora. The application will guide you through various text analysis features.

   Example
   ```
   Welcome to the NLTK Query Experimentation
   Please select an option:
   [1] Download and use the inaugural corpus from NLTK
   [2] Specify path to corpus
   Enter Selection (1-2) >> 2
   Enter full path to the Corpus: .Path/to/corpus
   Processing Files : 
   ['text1.txt', 'text2.txt', 'text3.txt', ...]
   Please wait ...
   ```

## Troubleshooting
   **Encoding Issues**: If you encounter encoding errors, ensure that the text files are properly encoded in UTF-8. You may specify a different encoding if needed.

   **Resource Not Found**: Ensure that NLTK resources are properly downloaded and available in the nltk_data directory.

## Contributing
   Feel free to contribute to this project by submitting issues or pull requests. For significant changes, please open an issue first to discuss what you would like to change.

## Contact
   For any questions or comments, please reach out to thorpebryce@gmail.com.