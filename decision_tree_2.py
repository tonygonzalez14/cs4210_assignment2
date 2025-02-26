#-------------------------------------------------------------------------
# AUTHOR: Tony Gonzalez
# FILENAME: decision_tree_2.py
# SPECIFICATION: Compares decision tree performance using different training datasets
# FOR: CS 4210 - Assignment #2
# TIME SPENT: 1 hour for coding
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#Importing some Python libraries
from sklearn import tree
import csv

dataSets = ['contact_lens_training_1.csv', 'contact_lens_training_2.csv', 'contact_lens_training_3.csv']

for ds in dataSets:

    dbTraining = []
    X = []
    Y = []

    #Reading the training data in a csv file
    with open(ds, 'r') as csvfile:
         reader = csv.reader(csvfile)
         for i, row in enumerate(reader):
             if i > 0: #skipping the header
                dbTraining.append(row)

    #Transform the original categorical training features to numbers and add to the 4D array X.
    #For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3, X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
    #--> add your Python code here
    for instance in dbTraining:
        row = []
        for value in range(4):
            match value:
                case 0:
                    if instance[value] == "Young":
                        row.append(0)
                    elif instance[value] == "Prepresbyopic":
                        row.append(1)
                    elif instance[value] == "Presbyopic":
                        row.append(2)
                case 1:
                    if instance[value] == "Myope":
                        row.append(0)
                    elif instance[value] == "Hypermetrope":
                        row.append(1)
                case 2:
                    if instance[value] == "No":
                        row.append(0)
                    elif instance[value] == "Yes":
                        row.append(1)
                case 3:
                    if instance[value] == "Reduced":
                        row.append(0)
                    elif instance[value] == "Normal":
                        row.append(1)
        X.append(row)

    #Transform the original categorical training classes to numbers and add to the vector Y.
    #For instance Yes = 1 and No = 2, Y = [1, 1, 2, 2, ...]
    #--> add your Python code here
    for instance in dbTraining:
        if instance[4] == "No":
            Y.append(0)
        elif instance[4] == "Yes":
            Y.append(1)

    total_accuracy = 0

    #Loop your training and test tasks 10 times here
    for i in range (10):

       #Fitting the decision tree to the data setting max_depth=5
       clf = tree.DecisionTreeClassifier(criterion = 'entropy', max_depth=5)
       clf = clf.fit(X, Y)

       #Read the test data and add this data to dbTest
       #--> add your Python code here
       dbTest = []

       # Reading the training data in a csv file
       with open('contact_lens_test.csv', 'r') as csvfile:
           reader = csv.reader(csvfile)
           for index, row in enumerate(reader):
               if index > 0:  # skipping the header
                   dbTest.append(row)

       numberCorrect = 0
       for data in dbTest:
           #Transform the features of the test instances to numbers following the same strategy done during training,
           #and then use the decision tree to make the class prediction. For instance: class_predicted = clf.predict([[3, 1, 2, 1]])[0]
           #where [0] is used to get an integer as the predicted class label so that you can compare it with the true label
           #--> add your Python code here

           testX = []
           testY = []

           row = []
           for value in range(4):
               match value:
                   case 0:
                       if data[value] == "Young":
                           row.append(0)
                       elif data[value] == "Prepresbyopic":
                           row.append(1)
                       elif data[value] == "Presbyopic":
                           row.append(2)
                   case 1:
                       if data[value] == "Myope":
                           row.append(0)
                       elif data[value] == "Hypermetrope":
                           row.append(1)
                   case 2:
                       if data[value] == "No":
                           row.append(0)
                       elif data[value] == "Yes":
                           row.append(1)
                   case 3:
                       if data[value] == "Reduced":
                           row.append(0)
                       elif data[value] == "Normal":
                           row.append(1)
           testX.append(row)

           if data[4] == "No":
            testY.append(0)
           elif data[4] == "Yes":
            testY.append(1)

           class_prediction = clf.predict(testX)[0]

           if class_prediction == testY[0]:
               numberCorrect += 1

       total_accuracy += numberCorrect / 8
       
    average_accuracy = total_accuracy / 10
    print(f"Final accuracy when training on {ds}: {average_accuracy}")

           #Compare the prediction with the true label (located at data[4]) of the test instance to start calculating the accuracy.
           #--> add your Python code here

    #Find the average of this model during the 10 runs (training and test set)
    #--> add your Python code here

    #Print the average accuracy of this model during the 10 runs (training and test set).
    #Your output should be something like that: final accuracy when training on contact_lens_training_1.csv: 0.2
    #--> add your Python code here




