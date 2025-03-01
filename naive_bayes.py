#-------------------------------------------------------------------------
# AUTHOR: Tony Gonzalez
# FILENAME: naive_bayes.py
# SPECIFICATION: Classification using Naive Bayes
# FOR: CS 4210- Assignment #2
# TIME SPENT: About 1 hour
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

# Importing some Python libraries
from sklearn.naive_bayes import GaussianNB
import csv

train_db = []

# Reading the data in a csv file
with open('weather_training.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: # Skipping the header
         train_db.append(row)

# Organize training data
X_train = []
Y_train = []
for row in train_db:

    # Convert values into numeric form
    temp_row = []
    for column_index in range(len(row)):
        if column_index == 0: # Skip day
            continue
        elif column_index == 1: # Outlook
            match row[column_index]:
                case "Sunny":
                    temp_row.append(1)
                case "Overcast":
                    temp_row.append(2)
                case "Rain":
                    temp_row.append(3)
        elif column_index == 2: # Temp
            match row[column_index]:
                case "Cool":
                    temp_row.append(1)
                case "Mild":
                    temp_row.append(2)
                case "Hot":
                    temp_row.append(3)
        elif column_index == 3: # Humidity
            match row[column_index]:
                case "Normal":
                    temp_row.append(1)
                case "High":
                    temp_row.append(2)
        elif column_index == 4: # Wind
            match row[column_index]:
                case "Weak":
                    temp_row.append(1)
                case "Strong":
                    temp_row.append(2)
        elif column_index == 5: # Label
            match row[column_index]:
                case "No":
                    Y_train.append(0)
                case "Yes":
                    Y_train.append(1)
    X_train.append(temp_row)

# Train model
clf = GaussianNB(var_smoothing=1e-9)
clf.fit(X_train, Y_train)

test_db = []

# Reading the data in a csv file
with open('weather_test.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         test_db.append(row)

# Organize test data
X_test = []
for row in test_db:

    # Convert values into numeric form
    temp_row = []
    for column_index in range(len(row)):
        if column_index == 0: # Skip day
            continue
        elif column_index == 1: # Outlook
            match row[column_index]:
                case "Sunny":
                    temp_row.append(1)
                case "Overcast":
                    temp_row.append(2)
                case "Rain":
                    temp_row.append(3)
        elif column_index == 2: # Temp
            match row[column_index]:
                case "Cool":
                    temp_row.append(1)
                case "Mild":
                    temp_row.append(2)
                case "Hot":
                    temp_row.append(3)
        elif column_index == 3: # Humidity
            match row[column_index]:
                case "Normal":
                    temp_row.append(1)
                case "High":
                    temp_row.append(2)
        elif column_index == 4: # Wind
            match row[column_index]:
                case "Weak":
                    temp_row.append(1)
                case "Strong":
                    temp_row.append(2)
        elif column_index == 5: # Label
            continue
    X_test.append(temp_row)

# Make predictions
predictions = clf.predict_proba(X_test)

# Print header
print(f"{'Day':<10}{'Outlook':<15}{'Temperature':<15}{'Humidity':<10}{'Wind':<10}{'PlayTennis':<15}{'Confidence':<10}")

# Print output
output = None
confidence = None
for row_index, row in enumerate(test_db):
    if predictions[row_index][0] > predictions[row_index][1] and predictions[row_index][0] >= 0.75: # No prediction
        output = "No"
        confidence = predictions[row_index][0]
    elif predictions[row_index][0] < predictions[row_index][1] and predictions[row_index][1] >= 0.75: # Yes prediction
        output = "Yes"
        confidence = predictions[row_index][1]
    else: # Not confident enough
        output = "N/A"
        confidence = max(predictions[row_index][0], predictions[row_index][1])

    # Only print predictions with over 0.75
    if confidence > 0.75:
        print(f"{row[0]:<10}{row[1]:<15}{row[2]:<15}{row[3]:<10}{row[4]:<10}{output:<15}{confidence:<10.2f}")