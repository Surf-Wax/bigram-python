# Simple Bigram Model by Bryce Thorpe
# I made this model to cement my understanding of this basic language model
#  and to lay the mental groundwork for understanding more complex models

import os
import nltk
import csv
from collections import defaultdict, Counter
from time import sleep
from prettytable import PrettyTable


# Download NLTK resources if not already present
def downloadResources():
    download_dir = os.path.join(os.getcwd(), 'nltk_data')
    nltk_resources = ['punkt']
    for resource in nltk_resources:
        try:
            nltk.data.find(f'{resource}' if resource != 'punkt' else f'tokenizers/{resource}')
        except LookupError:
            print(f"Downloading NLTK resource: {resource}")
            nltk.download(resource, download_dir=download_dir)
    
    # Set NLTK data path
    nltk_data_path = os.path.join(os.getcwd(), 'nltk_data')
    nltk.data.path.append(nltk_data_path)


# Train the bigram model on a string of text (small corpus)
def trainBigramModel():
    # Prompt the user for word to predict the next word
    while True:
      userString = input(f"Please input a string (max 255 characters): ").strip()
      # Check if the input is empty or exceeds the maximum length
      if len(userString) > 255:
          print(f"Input exceeds 255 characters. Please try again.")
      elif len(userString) == 0:
          print("Input cannot be empty. Please try again.")
      else:
          break  # Exit the loop if input is valid

    # Tokenize user input
    tokens = nltk.word_tokenize(userString.lower())

    ###  Create a list of bigrams ###
    bigrams = list(nltk.bigrams(tokens))

    # Create a dictionary of the bigrams/tokens and their counts
    bigramCounts = Counter(bigrams)
    unigramCounts = Counter(tokens)

    # Create a nested dictionary to store the probabilities 
    bigramProbabilities = defaultdict(lambda: defaultdict(float))

    # Calculate and store the probabilities
    #   (tuple)  (value)      (dict)
    for (w1, w2), count in bigramCounts.items():
        # Probability = the count of that bigram divided by the count of the first word (w1) in the bigram. 
        # This gives the probability of w2 given w1 (i.e., 𝑃𝑤2∣𝑤1)
        bigramProbabilities[w1][w2] = count / unigramCounts[w1]

    # Create a PrettyTable
    table = PrettyTable()
    table.field_names = ["Bigram", "Probability"]
    # Add the bigram probabilities to the table
    for w1 in bigramProbabilities:
        for w2 in bigramProbabilities:
            table.add_row([f"P({w2} | {w1})", f"{bigramProbabilities[w1][w2]:.2f}"])
    # Print the table
    print(table)

    # return the bigramProbabilties dictionary for other functions
    return bigramProbabilities


# Predict the next word using training data
def predictWord(bigramProbabilities):
    # Prompt the user for word to predict the next word
    while True:
      previousWord = input(f"Please input a valid word (max 17 characters): ").strip()
      # Check if the input is empty or exceeds the maximum length
      if len(previousWord) > 17:
          print(f"\nInput exceeds 17 characters. Please try again.")
      elif len(previousWord) == 0:
          print("\nInput cannot be empty. Please try again.")
      else:
          break  # Exit the loop if input is valid
        
    # Get the probabilities of the next words, given the previous word
    nextWordProbabilities = bigramProbabilities[previousWord]

    # If a bigram exists,
    if nextWordProbabilities:
        # Search the dictionary for the word with the largest probability value, return the word
        predictedNextWord = max(nextWordProbabilities, key=nextWordProbabilities.get)
        # Get the probability of the most likely next word
        predictedNextProbability = nextWordProbabilities[predictedNextWord]
        print(f"") 
        print(f"-> {predictedNextWord} <- (The most likely next word after '{previousWord}' is '{predictedNextWord}' with a probability of '{predictedNextProbability}')")
        print("")
    else:
        print("")
        print(f"-> No predictions available for the word '{previousWord}'.")
        print("")

# Write the PrettyTable data to a text file
def writeTable(table):
    with open('bigram_probabilities.txt', 'w') as txtfile:
        txtfile.write(table.get_string())

# Get a word from the user


if __name__ == '__main__':

    # Initialize userInput to -1
    userInput = -1

    # Download required resources (nltk)
    downloadResources()
 
    print("\nWelcome to my simple bigram implementation\n")

    # Train the bigram model on user input for predicting the next word
    curModel = trainBigramModel()

    while userInput < 2:
        # Gather user input
        userInput = int(input("\n[0] Train model on new text(corpus)\n[1] Predict word\n[2] Quit\nPlease select an option by entering a number: "))

        if userInput == 0:
            curModel = trainBigramModel()
        elif userInput == 1:
            predictWord(curModel)
        elif userInput == 2:
            print("Thank you!")
        else:
            print("Please enter a valid selection...\n")

