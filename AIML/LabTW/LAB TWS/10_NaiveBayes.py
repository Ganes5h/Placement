import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Read the data from the CSV file
df = pd.read_csv('fruits.csv')

# Print the dataset
print("Dataset:")
print(df)

# Split the data into features and labels
X = df[['Yellow', 'Sweet', 'Long']]
y = df['Fruit']

# Print the features and labels
print("\nFeatures:")
print(X)
print("\nLabels:")
print(y)

# Initialize the Naive Bayes classifier
model = MultinomialNB()

# Train the classifier
model.fit(X, y)

# Make predictions on the training set
predictions = model.predict(X)

# Calculate the accuracy
accuracy = accuracy_score(y, predictions)

# Generate the classification report
class_report = classification_report(y, predictions)

# Print the predictions, accuracy, and classification report
print("\nPredictions:")
print(predictions)
print("\nAccuracy:")
print(accuracy)
print("\nClassification Report:")
print(class_report)
