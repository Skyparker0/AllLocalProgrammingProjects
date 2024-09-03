import csv
import sys

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        -0 Administrative, an integer
        -1 Administrative_Duration, a floating point number
        -2 Informational, an integer
        -3 Informational_Duration, a floating point number
        -4 ProductRelated, an integer
        -5 ProductRelated_Duration, a floating point number
        -6 BounceRates, a floating point number
        -7 ExitRates, a floating point number
        -8 PageValues, a floating point number
        -9 SpecialDay, a floating point number
        -10 Month, an index from 0 (January) to 11 (December)
        -11 OperatingSystems, an integer
        -12 Browser, an integer
        -13 Region, an integer
        -14 TrafficType, an integer
        -15 VisitorType, an integer 0 (not returning) or 1 (returning)
        -16 Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """
    evidence = []
    labels = []
    
    with open(filename) as CSVfile:
        reader = csv.reader(CSVfile, delimiter="\t")
        lis = [row[0].split(',') for row in reader][1:]
        for row in lis:
            nE = row[:-1]   #newEvidence
            nL = row[-1]    #newLabel
            
            for index in [0,2,4,11,12,13,14]:  #ints
                nE[index] = int(nE[index])
                
            for index in [1,3,5,6,7,8,9]:  #floats
                nE[index] = float(nE[index])
                
            nE[10] = ['Jan', 'Feb', 'Mar', 'Apr','May','June','Jul', 'Aug','Sep','Oct','Nov', 'Dec']\
                .index(nE[10])
                
            nE[15] = 1 if nE[15] == 'Returning_Visitor' else 0
            
            nE[16] = 1 if nE[16] == 'TRUE' else 0
            
            nL = 1 if nL == 'TRUE' else 0
                
            evidence.append(nE)
            labels.append(nL)
            
    return (evidence, labels)
            


def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    neigh = KNeighborsClassifier(n_neighbors=1)
    neigh.fit(evidence,labels)
    return neigh


def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificty).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """
    totalPos = labels.count(1)
    totalNeg = labels.count(0)
    correctPosGuess = [labels[i] == predictions[i] == 1 for i in range(len(labels))].count(True)
    correctNegGuess = [labels[i] == predictions[i] == 0 for i in range(len(labels))].count(True)
    
    return (correctPosGuess/totalPos, correctNegGuess/totalNeg)


if __name__ == "__main__":
    main()
