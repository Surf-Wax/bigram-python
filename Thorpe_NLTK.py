import os
import nltk
from nltk.corpus import PlaintextCorpusReader, stopwords, inaugural
from time import sleep
from prettytable import PrettyTable

# Download NLTK resources if not already present
download_dir = os.path.join(os.getcwd(), 'nltk_data')
nltk_resources = ['stopwords', 'punkt']
for resource in nltk_resources:
    try:
        nltk.data.find(f'{resource}' if resource != 'punkt' else f'tokenizers/{resource}')
    except LookupError:
        print(f"Downloading NLTK resource: {resource}")
        nltk.download(resource, download_dir=download_dir)

# Download the nltk Inaugural Corpus if user selected to
def download_optional_corpus():
    nltk_resources = ['inaugural']
    for resource in nltk_resources:
        try:
            nltk.data.find(f'corpora/{resource}')
        except LookupError:
            print(f"Downloading NLTK resource: {resource}")
            nltk.download(resource, download_dir=download_dir)

# Set NLTK data path
nltk_data_path = os.path.join(os.getcwd(), 'nltk_data')
nltk.data.path.append(nltk_data_path)

# Initialize stopwords set
stopSet = set(stopwords.words('english'))

class NLTKQuery:
    ''' NLTK Query Class '''
    def textCorpusInit(self, thePath):
        if not os.path.isdir(thePath):
            return "Path is not a Directory"

        if not os.access(thePath, os.R_OK):
            return "Directory is not Readable"

        try:
            self.Corpus = PlaintextCorpusReader(thePath, '.*')
            print("Processing Files : ")
            print(self.Corpus.fileids())
            print("Please wait ...")
            self.rawText = self.Corpus.raw()
            self.tokens = nltk.word_tokenize(self.rawText)
            self.TextCorpus = nltk.Text(self.tokens)
        except Exception as e:
            print(f"Corpus Creation Failed: {e}")
            return f"Corpus Creation Failed: {e}"

        self.ActiveTextCorpus = True
        return "Success"

    def printCorpusLength(self):
        print("\n\nCorpus Text Length: ", '{:,}'.format(len(self.rawText)))

    def printTokensFound(self):
        print("\n\nTokens Found: ", '{:,}'.format(len(self.tokens)))

    def printVocabSize(self):
        print("\n\nCalculating Vocabulary Size...")
        uniqueTokenCnt = len(set(self.tokens))
        print('\nVocabulary Size: ', uniqueTokenCnt)

    def searchWordOccurrence(self):
        print("\n\nCompiling Top 100 Collocations ...")
        collocations = self.TextCorpus.collocation_list()
        for col, occurance in collocations:
            print(col, occurance)

        wordDict = {'Government': 0, 'President': 0, 'citizens': 0, 'World': 0, 'United': 0}
        print('\n\nSearching for test words: ', ', '.join(wordDict.keys()))
        for word in self.tokens:   
            if word in wordDict:
                wordDict[word] += 1

        print("\nWords Found: ")
        for word, occurances in wordDict.items():
            print(word, occurances)

    def generateConcordance(self):
        myWord = input("\n\nEnter word to Concord: ")
        if myWord:
            print("Compiling First 100 Concordance Entries ...")
            print("\n", self.TextCorpus.concordance(myWord, 200, 100))

    def generateSimilarities(self):
        myWord = input("\n\nEnter seed word: ")
        if myWord:
            print("Compiling First 200 Similarity Entries ...")
            print("\n", self.TextCorpus.similar(myWord))

    def printWordIndex(self):
        myWord = input("\n\nFind first occurrence of what Word?: ")
        if myWord:
            print("Searching for first occurrence of: ", myWord)
            count = 0
            for i, word in enumerate(self.tokens):
                if myWord in word:
                    count += 1
                    print(str(count) + ': Found at index ' + str(i))
                    break
            if count == 0:
                print("Word not found in corpus")

    def printVocabulary(self):
        print("\n\nCompiling Vocabulary Frequencies")
        tbl = PrettyTable(["Vocabulary", "Occurs"])
        vocabDict = {}
        for word in self.tokens:
            if word.lower() not in stopSet:
                vocabDict[word] = vocabDict.get(word, 0) + 1
        for vocab, occurance in vocabDict.items():
            tbl.add_row([vocab, occurance])
        tbl.sortby = 'Occurs'
        tbl.reversesort = False
        print(tbl)

def printMenu():
    print("==========NLTK Query Options =========")
    print("[1]    Print Length of Corpus")
    print("[2]    Print Number of Tokens Found")
    print("[3]    Print Vocabulary Size")
    print("[4]    Search for Word Occurrence")
    print("[5]    Generate Concordance")
    print("[6]    Generate Similarities")
    print("[7]    Print Word Index")
    print("[8]    Print Vocabulary")
    print()
    print("[0]    Exit NLTK Experimentation")
    print()

def getUserSelection():
    printMenu()
    while True:
        try:
            menuSelection = int(input('Enter Selection (0-8) >> '))
            if menuSelection in range(0, 9):
                return menuSelection
            else:
                print('Invalid input. Enter a value between 0-8.')
        except ValueError:
            print('Invalid input. Enter a value between 0-8.')

if __name__ == '__main__':
    print("Welcome to the NLTK Query Experimentation")
    print("Please select an option:")
    print("[1] Download and use the inaugural corpus from NLTK")
    print("[2] Specify path to Corpus")
    userChoice = input("Enter Selection (1-2) >> ")

    oNLTK = NLTKQuery()
    result = ""

    if userChoice == '1':
        download_optional_corpus()
        oNLTK.Corpus = inaugural
        oNLTK.rawText = inaugural.raw()
        oNLTK.tokens = nltk.word_tokenize(oNLTK.rawText)
        oNLTK.TextCorpus = nltk.Text(oNLTK.tokens)
        result = "Success"
    elif userChoice == '2':
        userSpecifiedPath = input("Enter full path to the Corpus: ")
        result = oNLTK.textCorpusInit(userSpecifiedPath)
    else:
        print("Invalid selection. Exiting.")
        result = "Failure"

    if result == "Success":
        menuSelection = -1
        while menuSelection != 0:
            if menuSelection != -1:
                input('Press Enter to continue...')
            menuSelection = getUserSelection()
            if menuSelection == 1:
                oNLTK.printCorpusLength()
            elif menuSelection == 2:
                oNLTK.printTokensFound()
            elif menuSelection == 3:
                oNLTK.printVocabSize()
            elif menuSelection == 4:
                oNLTK.searchWordOccurrence()
            elif menuSelection == 5:
                oNLTK.generateConcordance()
            elif menuSelection == 6:
                oNLTK.generateSimilarities()
            elif menuSelection == 7:
                oNLTK.printWordIndex()
            elif menuSelection == 8:
                oNLTK.printVocabulary()
            elif menuSelection == 0:
                print("Goodbye")
            else:
                print("Unexpected error condition")
            sleep(3)
    else:
        print("Closing NLTK Query Experimentation")

