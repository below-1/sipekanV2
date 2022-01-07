from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.naive_bayes import MultinomialNB
import csv
import numpy as np

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