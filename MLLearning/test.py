from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
import matplotlib.pyplot as plt

# Sufficient dataset for meaningful split
X = np.array([800, 1000, 1200, 1500, 1800, 2100, 2500]).reshape(-1, 1)
y = np.array([160, 200, 240, 300, 360, 420, 500])

# Split the data with enough samples for testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error (MSE): {mse}")
print(f"R-squared (R²): {r2}")

# Plot the results
plt.scatter(X_train, y_train, color='blue', label="Training data")
plt.scatter(X_test, y_test, color='green', label="Test data")
plt.plot(X, model.predict(X), color='red', label="Regression line")
plt.xlabel("House Size (sq ft)")
plt.ylabel("Price ($1000)")
plt.legend()
plt.title("Train-Test Split with Sufficient Data")
plt.show()
