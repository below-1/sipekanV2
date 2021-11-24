from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.naive_bayes import MultinomialNB
import csv
import numpy as np

FILENAME = 'app/data.csv'

def load_data():
    data = []
    with open(FILENAME) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    data = data[1:]

    arr = []
    for i, row in enumerate(data):
        if i == 0:
            continue
        x = [ 0 if x == 'FALSE' else 1 for x in row[2:-1] ]

        # Skip row with all passed components
        if sum(x) == len(x):
            continue

        y = 0 if row[-1] == 'TIDAK LULUS' else 1
        x.append(y)
        new_row = [ int(row[0]) ]
        new_row.extend(x)
        arr.append(new_row)
    data = np.array(arr)
    return data

def build_classifier():
    data = load_data()
    # Skip id
    X = data[:, 1:-1]
    y = data[:, -1]
    clf = MultinomialNB()
    clf.fit(X, y)
    return clf

def test_method(random_state=8, test_size=0.3):
    data = load_data()

    X = data[:, :-1]
    y = data[:, -1]

    X_train, X_test, y_train, y_test = train_test_split(
        X, 
        y, 
        test_size=test_size,
        random_state=random_state
    )

    clf = MultinomialNB()

    # Skip id
    clf.fit(X_train[:, 1:], y_train)

    # Collect test data's ids
    test_ids = list(X_test[:, 1])

    y_pred = clf.predict(X_test[:, 1:])
    tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()
    acc = (tp + tn) / (tn + fp + fn + tp)
    print(f'{acc}')
    err_rate = (fn + fp) / (tn + fp + fn + tp)
    print(f'{err_rate}')

    return {
        'tp': tp,
        'tn': tn,
        'fn': fn,
        'fp': fp,
        'acc': acc,
        'err_rate': err_rate
    }


clf = build_classifier()
def mult_nb(_xs):
    nattr = len(_xs)
    xs = np.array(_xs).reshape(( 1, nattr ))
    result, *_ = clf.predict(xs)
    return result
