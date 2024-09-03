import nltk
import sys
import os

FILE_MATCHES = 2
SENTENCE_MATCHES = 3


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python questions.py corpus")

    # Calculate IDF values across files
    files = load_files(sys.argv[1])
    file_words = {
        filename: tokenize(files[filename])
        for filename in files
    }
    file_idfs = compute_idfs(file_words)

    # Prompt user for query
    query = set(tokenize(input("Query: ")))

    # Determine top file matches according to TF-IDF
    filenames = top_files(query, file_words, file_idfs, n=FILE_MATCHES)

    # Extract sentences from top files
    sentences = dict()
    for filename in filenames:
        for passage in files[filename].split("\n"):
            for sentence in nltk.sent_tokenize(passage):
                tokens = tokenize(sentence)
                if tokens:
                    sentences[sentence] = tokens

    # Compute IDF values across sentences
    idfs = compute_idfs(sentences)

    # Determine top sentence matches
    matches = top_sentences(query, sentences, idfs, n=SENTENCE_MATCHES)
    for match in matches:
        print(match)


def load_files(directory):
    """
    Given a directory name, return a dictionary mapping the filename of each
    `.txt` file inside that directory to the file's contents as a string.
    """
    fileDic = {}
    
    for file in os.listdir(directory):
        name = file
        with open(os.path.join(directory,file), encoding="utf8") as openFile:
            fileDic[name] = openFile.read()
            
    return fileDic


def tokenize(document):
    """
    Given a document (represented as a string), return a list of all of the
    words in that document, in order.

    Process document by coverting all words to lowercase, and removing any
    punctuation or English stopwords.
    """
    import string
    lst = nltk.word_tokenize(document.lower())
    removevals = [punct for punct in string.punctuation] + nltk.corpus.stopwords.words("english")
    lst = [word for word in lst if word not in removevals]
    return lst


def compute_idfs(documents):
    """
    Given a dictionary of `documents` that maps names of documents to a list
    of words, return a dictionary that maps words to their IDF values.

    Any word that appears in at least one of the documents should be in the
    resulting dictionary.
    """
    import math
    
    numDocs = len(documents)
    IDFS = {}
    
    
    def docFreq(term):
        df = 0
        for doc in documents.values():
            if term in doc:
                df += 1
        return df
    
    for doc in documents.values():
        for word in doc:
            if word not in IDFS:
                IDFS[word] = math.log(numDocs/docFreq(word))
                
    return IDFS


def top_files(query, files, idfs, n):
    """
    Given a `query` (a set of words), `files` (a dictionary mapping names of
    files to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the filenames of the the `n` top
    files that match the query, ranked according to tf-idf.
    """
    def tf_idf(term,filename):
        tf = files[filename].count(term)
        idf = idfs[term]
        return tf * idf
    
    fileValues = {fileName:0 for fileName in files}
    
    for file in files:
        for word in query:
            fileValues[file] += tf_idf(word, file)
    
    sortedDict = {k: v for k, v in sorted(fileValues.items(), key=lambda item: item[1])}
    
    return list(sortedDict.keys())[-n:]

def top_sentences(query, sentences, idfs, n):
    """
    Given a `query` (a set of words), `sentences` (a dictionary mapping
    sentences to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the `n` top sentences that match
    the query, ranked according to idf. If there are ties, preference should
    be given to sentences that have a higher query term density.
    """
    sentanceValues = {sentenceName:0 for sentenceName in sentences}
    
    for sentence in sentences:
        for word in query:
            if word in sentences[sentence]:
                sentanceValues[sentence] += idfs[word] + 0.001
    
    sortedDict = {k: v for k, v in sorted(sentanceValues.items(), key=lambda item: item[1])}
    
    return list(sortedDict.keys())[-n:]


if __name__ == "__main__":
    main()
