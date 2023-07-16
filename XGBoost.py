import pandas as pd
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.tree import DecisionTreeRegressor

# Create a regression dataset
X, y = make_regression(n_samples=100, n_features=1, noise=0.1, random_state=42)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Decision Tree Regressor
model = DecisionTreeRegressor()

# Train the model on the training data
model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test)

# Evaluate the mean squared error of the model
mse = mean_squared_error(y_test, y_pred)

# Create a DataFrame to display the results
results_df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})

# Print the results
print(results_df)
print("\nMean Squared Error:", mse)
