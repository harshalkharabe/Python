import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Sample data (house areas in square meters and prices)
areas = np.array([50, 70, 100, 120, 150,160,190,204,215,245,270,299,396,456,888]).reshape(-1, 1)  # Features
prices = np.array([150000, 200000, 280000, 320000, 400000, 410000, 470000, 500000,525000,570000,600000,1234000,1256000, 1236700,45678000])  # Labels

# Create and train the model
model = LinearRegression()
model.fit(areas, prices)

# Model parameters
print(f"Slope (w): {model.coef_[0]}")
print(f"Intercept (b): {model.intercept_}")

# Make a prediction
predicted_price = model.predict([[110]])
print(f"Predicted price for a 110 sqm house: ${predicted_price[0]:,.2f}")

# Plotting
plt.scatter(areas, prices, color='blue', label='Actual Prices')
plt.plot(areas, model.predict(areas), color='red', label='Prediction Line')
plt.xlabel("Area (Square Meters)")
plt.ylabel("Price (USD)")
plt.legend()
plt.show()


# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.linear_model import LinearRegression
# from sklearn.model_selection import train_test_split

# # Simple dataset
# data = {
#     'Size': [750, 800, 850, 1000, 1200],
#     'Price': [150, 170, 180, 210, 240]
# }
# df = pd.DataFrame(data)
# print(df)

# plt.scatter(df['Size'], df['Price'], color='blue')
# plt.xlabel("Size (sq ft)")
# plt.ylabel("Price ($1000)")
# plt.title("House Size vs Price")
# plt.show()

# X = df[['Size']]  # Features (independent variable)
# y = df['Price']   # Labels (dependent variable)

# # Split into training and testing sets (80% training, 20% testing)
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# model = LinearRegression()
# model.fit(X_train, y_train)

# predictions = model.predict(X_test)
# print("Predicted Prices:", predictions)
# print("Actual Prices:", list(y_test))

# # Visualize predictions
# plt.scatter(X_test, y_test, color='red', label='Actual Prices')
# plt.plot(X_test, predictions, color='blue', label='Predicted Prices')
# plt.legend()
# plt.show()

# print("Model Coefficient (Slope):", model.coef_[0])
# print("Model Intercept:", model.intercept_)

# print(f"Prediction Formula: Price = {model.coef_[0]} * Size + {model.intercept_}")
