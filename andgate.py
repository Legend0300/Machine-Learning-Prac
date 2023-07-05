import numpy as np
import numpy as np
from sklearn.linear_model import SGDRegressor , LogisticRegression  ,LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,classification_report,accuracy_score
# Define the input features and target variable for the AND gate
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 0, 0, 1])

# Return the training set
X_train = X
y_train = y

print("X_train:")
print(X_train)
print("y_train:")
print(y_train)

sgdr = LogisticRegression(penalty='none')



sgdr.fit(X_train , y_train)

print(sgdr.predict([[1, 1]]))


