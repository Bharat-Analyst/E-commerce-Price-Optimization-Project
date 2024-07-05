import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Step 1: Load the data
# For demonstration, let's use a synthetic dataset
# You would replace this with loading your actual data
data_url = 'File--path' 
data = pd.read_csv(data_url)

# Step 2: Data Preprocessing
# Assuming 'total_bill' as the price, 'size' as the quantity sold
data = data[['total_bill', 'size', 'tip']]
data.rename(columns={'total_bill': 'price', 'size': 'quantity'}, inplace=True)

# Step 3: Feature Engineering
# Create additional features if necessary
data['price_per_person'] = data['price'] / data['quantity']

# Step 4: Split the data
X = data[['price_per_person', 'quantity']]
y = data['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 6: Make predictions
y_pred = model.predict(X_test)

# Step 7: Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

print(f"Mean Absolute Error: {mae}")
print(f"Root Mean Squared Error: {rmse}")

# Step 8: Dynamic Pricing
# Function to calculate optimized price based on the model
def calculate_optimized_price(quantity):
    price_per_person = model.coef_[0]  # Assuming single feature model
    return price_per_person * quantity

# Example usage
optimized_price = calculate_optimized_price(5)
print(f"Optimized Price for quantity 5: {optimized_price}")
