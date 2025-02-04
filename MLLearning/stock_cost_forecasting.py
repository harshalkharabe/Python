# Importing essential libraries
import numpy as np  # For numerical operations and arrays
import pandas as pd  # For handling datasets
import matplotlib.pyplot as plt  # For visualizing data
from sklearn.model_selection import train_test_split  # Splitting data into training/testing sets
from sklearn.linear_model import LinearRegression  # Linear regression model
from sklearn.metrics import mean_squared_error  # For evaluating model performance

# Step 1: Sample stock data (you can use a real dataset instead)
data = {
    "Day": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],  # Independent variable (time)
    "Stock Price": [100, 101, 102, 103, 105, 108, 109, 112, 115, 120],  # Dependent variable (stock price)
}

df = pd.DataFrame(data)  # Convert dictionary to Pandas DataFrame
print("Dataset Preview:\n", df)

# Step 2: Split data into features (X) and labels (y)
X = df[['Day']]  # Feature set (independent variable)
y = df['Stock Price']  # Target variable (dependent variable)

# Step 3: Split data into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# train_test_split(): Splits the data into training/testing sets
# test_size=0.2 means 20% of the data is used for testing
# random_state ensures consistent results
# Step 4: Create a Linear Regression model
model = LinearRegression()  # Initialize the Linear Regression model

# Step 5: Train the model using the training data
model.fit(X_train, y_train)  
# .fit(): Trains the model by finding the best fit line for the given data

# Step 6: Predict stock prices for test data
predictions = model.predict(X_test)  
# .predict(): Makes predictions based on the test input

print("\nPredicted Stock Prices for Test Data:", predictions)

# Step 7: Model evaluation using Mean Squared Error (MSE)
mse = mean_squared_error(y_test, predictions)  
# mean_squared_error(): Evaluates prediction accuracy by measuring average squared error
print("\nMean Squared Error (MSE):", mse)

# Step 8: Visualization of Training Data and Best Fit Line
plt.scatter(X_train, y_train, color='blue', label="Training Data")  # Plot actual data points
plt.plot(X_train, model.predict(X_train), color='red', label="Best Fit Line")  # Plot best fit line
plt.title("Stock Price Prediction using Linear Regression")
plt.xlabel("Day")
plt.ylabel("Stock Price")
plt.legend()
plt.show()
