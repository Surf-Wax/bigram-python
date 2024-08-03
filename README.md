# Simple Stochastic Bigram Model by Bryce Thorpe

## Overview

This Simple Stochastic Bigram Model is a basic implementation of a bigram language model created to illustrate the fundamental concepts of probabilistic text modeling. This Python script utilizes the Natural Language Toolkit (NLTK) library to train a bigram model based on user-provided text and predict the next word given an input word. 

The model supports temperature-based adjustments to influence the randomness of predictions and produce different outputs even for the same input, reflecting the underlying probability distribution rather than always choosing the most probable option.

## Purpose

The script is designed to:
- Demonstrate the application of bigram language models for text prediction.
- Provide a practical example of how temperature scaling affects the randomness of predictions.
- Serve as an educational tool for understanding bigram models and basic probabilistic text prediction techniques.

This script was created for my own learning and practical application.

## Features

- **Bigram Model Training**: Trains a bigram model on user-provided text, calculating the probabilities of word pairs.
- **Temperature-Based Prediction**: Allows adjustment of prediction randomness using temperature scaling, affecting the likelihood of next word predictions.
- **User Input Validation**: Ensures valid user inputs for text and temperature, with checks for length and value constraints.
- **Probability Normalization**: Computes and normalizes adjusted probabilities to ensure valid prediction distributions.
- **PrettyTable Integration**: Displays bigram probabilities in a well-formatted table for easy viewing.
- **Nix Flakes Integration**: Uses Nix flakes to create a development shell that manages Python versions and external libraries automatically.

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
3. **Predict Words**:
    - Input a word (up to 17 characters) for which you want to predict the next word.
    - Provide a temperature value (between 0 and 2) to adjust prediction randomness.
    - The script will display the most likely next word based on the trained model and the provided temperature.
4. **Options**:
    - `[0] Train model on new text (corpus)`: Re-train the model with a new text input.
    - `[1] Predict word`: Predict the next word given an input word.
    - `[2] Quit`: Exit the program.

**Example Output:**
```
    Downloading NLTK resource: punkt
    [nltk_data] Downloading package punkt to
    [nltk_data]     /home/bear/Documents/dev/bigram-python/nltk_data...
    [nltk_data]   Package punkt is already up-to-date!
    
    Welcome to my simple bigram implementation
    
    Please input a string (max 255 characters): hello hello hello hello govnah
    +------------------+-------------+
    |      Bigram      | Probability |
    +------------------+-------------+
    | P(hello | hello) |     0.75    |
    +------------------+-------------+
    
    [0] Train model on new text(corpus)
    [1] Predict word
    [2] Quit
    Please select an option by entering a number: 1
    Please input a valid word (max 17 characters): hello
    Please input a temperature (0<x<2): .1
    
    -> hello <- (I've predicted the next word after 'hello' to be 'hello' with a probability of '0.999983065198984')
    
    
    [0] Train model on new text(corpus)
    [1] Predict word
    [2] Quit
    Please select an option by entering a number: 1
    Please input a valid word (max 17 characters): hello
    Please input a temperature (0<x<2): 1.9
    
    -> govnah <- (I've predicted the next word after 'hello' to be 'govnah' with a probability of '0.35934296642401403')
    
    
    [0] Train model on new text(corpus)
    [1] Predict word
    [2] Quit
    Please select an option by entering a number: 2
    Thank you!
```

## Contact
   For any questions or comments, please reach out to thorpebryce@gmail.com.

