# Implementation of Find S algorithm
import csv

# Reading the data from the CSV file
a = []
with open('enjoysports.csv', 'r') as csvfile:
    next(csvfile)  # Skip the header row
    for row in csv.reader(csvfile):
        a.append(row)

# Printing the dataset and the total number of training instances
print(a)
print("\nThe total number of training instances are:", len(a))

# Number of attributes in the dataset
num_attribute = len(a[0]) - 1
print("\nThe initial hypothesis is:")

# Initializing the hypothesis
hypothesis = ['0'] * num_attribute
print(hypothesis)

# Find-S algorithm
for i in range(len(a)):
    if a[i][num_attribute] == 'yes':
        print("\nInstance", i + 1, "is", a[i], "and is Positive Instance")
        for j in range(num_attribute):
            if hypothesis[j] == '0' or hypothesis[j] == a[i][j]:
                hypothesis[j] = a[i][j]
            else:
                hypothesis[j] = '?'
        print("The hypothesis for the training instance", i + 1, "is:", hypothesis, "\n")
    else:
        print("\nInstance", i + 1, "is", a[i], "and is Negative Instance Hence Ignored")
        print("The hypothesis for the training instance", i + 1, "is:", hypothesis, "\n")

print("\nThe Maximally specific hypothesis for the training instance is", hypothesis)
