import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("Netflix Userbase.csv")
print(df.head())

X = df[['Monthly Revenue', 'Age']]
y = df['Subscription Type']

print(X[0:5])
print(y[0:5])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=100)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = LogisticRegression(penalty='none')
model.fit(X_train, y_train)

predictions = model.predict(X_test)
print(predictions)
