import pandas as pd
# From a CSV file
df = pd.read_csv('data.csv')

# From an Excel file
df = pd.read_excel('data.xlsx')

# From a SQL database
import sqlite3
conn = sqlite3.connect('database.db')
df = pd.read_sql_query('SELECT * FROM table_name', conn)
conn.close()

# View the first few rows
df.head()

# View the last few rows
df.tail()

# Get information about the columns
df.info()

# Descriptive statistics
df.describe()

# Accessing specific columns
df['column_name']

# Filtering rows based on conditions
df[df['column_name'] > 10]


# Handling missing values
df.dropna()  # Drop rows with missing values
df.fillna(value)  # Fill missing values with a specific value

# Removing duplicates
df.drop_duplicates()

# Encoding categorical variables
encoded_df = pd.get_dummies(df, columns=['categorical_column'])

# Feature scaling
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaled_df = scaler.fit_transform(df)


# Selecting specific columns
selected_columns = ['column1', 'column2']
df_selected = df[selected_columns]

# Selecting columns based on conditions
df_filtered = df[df['column_name'] > 10]

# Removing irrelevant columns
df.drop(['column1', 'column2'], axis=1, inplace=True)



## axis == 0 vertical , axois == 1 horizontal 
from sklearn.model_selection import train_test_split
X = df.drop('target_column', axis=1)
y = df['target_column']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


from sklearn.svm import SVC
model = SVC()
model.fit(X_train, y_train)


y_pred = model.predict(X_test)

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, y_pred)
