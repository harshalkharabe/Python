import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load sample data
data = pd.read_csv('D:\TUTORIAL\PYTHON FULL STACK\PYTHON\MLLearning\customer_data.csv')  # Assuming you have a CSV file

# Assume the data has columns 'Age', 'Salary', and 'BoughtProduct' (0 = No, 1 = Yes)
X = data[['Age', 'Salary']]  # Features
y = data['BoughtProduct']  # Labels

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Train a Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Evaluate model accuracy
accuracy = accuracy_score(y_test, predictions)
print(f"Model accuracy: {accuracy * 100}%")
