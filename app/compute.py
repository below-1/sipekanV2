from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import csv
import numpy as np

filename = 'app/data.csv'
data = []
with open(filename) as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        data.append(row)
data = data[1:]

arr = []
for i, row in enumerate(data):
    if i == 0:
        continue
    x = [ 0 if x == 'FALSE' else 1 for x in row[2:-1] ]
    y = 0 if row[-1] == 'TIDAK LULUS' else 1
    x.append(y)
    arr.append(x)
data = np.array(arr)

X = data[:, :-1]
y = data[:, -1]

# X_train, X_test, y_train, y_test = train_test_split(
#     X, 
#     y, 
#     test_size=0.3,
    # random_state=8)

clf = MultinomialNB()
clf.fit(X, y)

def mult_nb(_xs):
    nattr = len(_xs)
    xs = np.array(_xs).reshape(( 1, nattr ))
    result, *_ = clf.predict(xs)
    return result
