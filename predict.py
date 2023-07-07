import numpy as np
from sklearn.linear_model import SGDRegressor , LinearRegression , LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

games_data = np.array([
    [59.99, 2018, 10.5, 1000],  # price, release date, game size, sales
    [39.99, 2020, 8.2, 800],
    [49.99, 2019, 12.1, 1200],
    [29.99, 2021, 9.5, 500],
    [19.99, 2017, 7.5, 300],
    [9.99, 2016, 5.5, 100],
    [69.99, 2015, 15.5, 1500],
    [79.99, 2014, 20.5, 2000],
    [89.99, 2013, 25.5, 2500],
    [99.99, 2012, 30.5, 3000],
    [109.99, 2011, 35.5, 3500],
    [119.99, 2010, 40.5, 4000],
    [129.99, 2009, 45.5, 4500],
    [139.99, 2008, 50.5, 5000],
])

X = games_data[:, 1:]
y_2d = games_data[:, :1]
y = y_2d.reshape(-1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

sgdr = LinearRegression()
sgdr.fit(X_train, y_train)


print(" test data: " + str(y_test))

y_pred_sgd = sgdr.predict(X_test)
print("Predicted prices:")
for pred in y_pred_sgd:
    print(pred)


from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Calculate evaluation metrics
mse = mean_squared_error(y_test, y_pred_sgd)
mae = mean_absolute_error(y_test, y_pred_sgd)
r2 = r2_score(y_test, y_pred_sgd)

# Print the evaluation metrics
print("Mean Squared Error:", mse)
print("Mean Absolute Error:", mae)
print("R-squared Score:", r2)

