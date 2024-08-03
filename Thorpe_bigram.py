import os
import nltk
from collections import defaultdict, Counter
from time import sleep
from prettytable import PrettyTable

# Download NLTK resources if not already present
download_dir = os.path.join(os.getcwd(), 'nltk_data')
nltk_resources = ['punkt']
for resource in nltk_resources:
    try:
        nltk.data.find(f'{resource}' if resource != 'punkt' else f'tokenizers/{resource}')
    except LookupError:
        print(f"Downloading NLTK resource: {resource}")
        nltk.download(resource, download_dir=download_dir)


if __name__ == '__main__':
    print("Welcome to my simple bigram implementation")

    # Gather user input
    userString = input("Please input a string of text:")

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

    # Print out the bigram probabilities
    for w1 in bigramProbabilities:
        for w2 in bigramProbabilities:
            print(f"P({w2} | {w1}) = {bigramProbabilities[w1][w2]:.4f}")

    # Prompt the user for word to predict the next word
    previousWord = input("Input a word to predict the next word")
    # Get the probabilities of the next words, given the previous word
    nextWordProbabilities = bigramProbabilities[previousWord]

    # If a bigram exists,
    if nextWordProbabilities:
        # Search the dictionary for the word with the largest probability value, return the word
        predictedNextWord = max(nextWordProbabilities, key=nextWordProbabilities.get)
        # Get the probability of the most likely next word
        predictedNextProbability = nextWordProbabilities[predictedNextWord]
        
        print(f"The most likely next word after '{previousWord}' is '{predictedNextWord}' with a probability of '{predictedNextProbability}'")
    else:
        print(f"No predictions available for the word '{previousWord}'.")
