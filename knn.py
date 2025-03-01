#-------------------------------------------------------------------------
# AUTHOR: Tony Gonzalez
# FILENAME: knn.py
# SPECIFICATION: Computes the LOO-CV Error Rate
# FOR: CS 4210- Assignment #2
# TIME SPENT: About 1 hour
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#Importing some Python libraries
from sklearn.neighbors import KNeighborsClassifier
import csv

db = []

#Reading the data in a csv file
with open('email_classification.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)

# Allow each instance to be your test set (LOO)
n_incorrect = 0
for cv_iteration in range(len(db)):

    # Train X and Train Y
    X = []
    Y = []
    # Iterate through each row and add to training sets
    for row_index, row in enumerate(db):
        # Skip the test set (LOO)
        if row_index == cv_iteration:
            continue

        # Add training data
        temp_row = []
        for column in range(21):
            if column < 20: # Features
                temp_row.append(float(row[column]))
            else: # Label
                if row[column] == "ham": # No
                    Y.append(0.0)
                else: # Yes
                    Y.append(1.0)
        X.append(temp_row)

    # Add testing data
    testSample = [[]]
    testLabel = []
    for column in range(21):
        if column < 20: # Features
            testSample[0].append(float(db[cv_iteration][column]))
        else: # Label
            if db[cv_iteration][column] == "ham":
                testLabel.append(0.0)
            else:
                testLabel.append(1.0)

    clf = KNeighborsClassifier(n_neighbors=1, p=2)
    clf = clf.fit(X, Y)

    class_prediction = clf.predict(testSample)

    if class_prediction != testLabel:
        n_incorrect += 1

# Final Error
print(f"LOO-CV Error Rate: {n_incorrect/len(db)}")
