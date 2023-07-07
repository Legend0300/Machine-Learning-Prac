import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv("Salary_Data.csv")

X = df['YearsExperience'].values.reshape(-1, 1)
y = df['Salary'].values


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=100)


model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
print("x: "  +str( predictions) + "y: "+ str(y_test))


# Calculate mean squared error
mse = mean_squared_error(y_test, predictions)

# Calculate root mean squared error
rmse = np.sqrt(mse)

# Calculate R-squared score
r2 = r2_score(y_test, predictions)

# Print the evaluation metrics
print("Mean Squared Error:", mse)
print("Root Mean Squared Error:", rmse)
print("R-squared Score:", r2)