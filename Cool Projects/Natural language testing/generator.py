import markovify
import sys
import os
# # Read text from file
# if len(sys.argv) != 2:
#     sys.exit("Usage: python generator.py sample.txt")
# with open(sys.argv[1]) as f:
#     text = f.read()
directory = 'C:/Users/batte/OneDrive/_Parker/Python/Cool Projects/Natural language testing/corpus'

allText = ""

for file in os.listdir(directory):
    name = file
    with open(os.path.join(directory,file), encoding="utf8") as openFile:
        allText += openFile.read()

def tokenize(document):
    """
    Given a document (represented as a string), return a list of all of the
    words in that document, in order.

    Process document by coverting all words to lowercase, and removing any
    punctuation or English stopwords.
    """
    import string
    import nltk
    lst = document.lower().split()
    removevals = [punct for punct in string.punctuation]# + nltk.corpus.stopwords.words("english")
    lst = [word for word in lst if word not in removevals]
    return lst

# Train model
text_model = markovify.Text(' '.join(tokenize(allText)), 2)

# Generate sentences
print()
for i in range(1):
    print("\t" + text_model.make_sentence())