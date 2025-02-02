import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Simple dataset
data = {
    'Size': [750, 800, 850, 1000, 1200],
    'Price': [150, 170, 180, 210, 240]
}
df = pd.DataFrame(data)
print(df)

plt.scatter(df['Size'], df['Price'], color='blue')
plt.xlabel("Size (sq ft)")
plt.ylabel("Price ($1000)")
plt.title("House Size vs Price")
plt.show()

X = df[['Size']]  # Features (independent variable)
y = df['Price']   # Labels (dependent variable)

# Split into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
print("Predicted Prices:", predictions)
print("Actual Prices:", list(y_test))

# Visualize predictions
plt.scatter(X_test, y_test, color='red', label='Actual Prices')
plt.plot(X_test, predictions, color='blue', label='Predicted Prices')
plt.legend()
plt.show()

print("Model Coefficient (Slope):", model.coef_[0])
print("Model Intercept:", model.intercept_)

print(f"Prediction Formula: Price = {model.coef_[0]} * Size + {model.intercept_}")
