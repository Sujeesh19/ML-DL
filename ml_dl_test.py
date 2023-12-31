# -*- coding: utf-8 -*-
"""ML-DL_test.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1k0Y9RlrktPjkf_deu_BlyJHgY1bbdSyN

#MCQs

* Q1. Ans - B) 12
* Q2. Ans  - A) 0
* Q3. Ans - A) 0
* Q4 Ans - A) Image classification
* Q5 Ans -  A)  It reduces the dataset to 10 features
* Q6. Ans - C) The cumulative reward obtained from 100 episodes.
"""

# Question 1: Binary Classification with scikit-learn
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Create a dummy dataset

data = pd.DataFrame({
    'Age': [25, 30, 35, 40, 45, 50, 55, 66, 65, 70],
    'Income': [40000, 45000, 60000, 80000, 90000, 75600, 55000, 60900, 50008, 45000],
    'Buy': [1, 0, 1, 1, 0, 1, 0, 0, 0, 1]
})
# Selecting independet and dependent values
x = data.iloc[:, [0,1]].values # independent
y = data.iloc[:,-1].values # dependent

y = y.reshape(y.shape[0], 1) # reshaping

# splitting the dataset
x_train, x_test, y_train, y_test = train_test_split(x,y,random_state=7,test_size=0.2)

# Building model
log = LogisticRegression()
log.fit(x_train, y_train)

# making predictions
predictions = log.predict(x_test)

# accuracy and classification report
acc = accuracy_score(predictions, y_test)
report = classification_report(predictions, y_test)
print("Accuracy Score ",acc)
print("Classification Report")
print(report)

# Question 2: Multiclass Classification with Dummy Data
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

# Create a dummy dataset
data = pd.DataFrame({
    'Weight (grams)': [120, 150, 130, 140, 180, 200, 160, 190, 170, 110],
    'Color': [1, 2, 1, 2, 3, 2, 3, 1, 2, 3],
    'Fruit': ['Apple', 'Banana', 'Apple', 'Banana', 'Orange', 'Banana', 'Orange', 'Apple', 'Banana', 'Apple']
})

# Selecting independet and dependent values
x = data.iloc[:, [0,1]].values # independent
y = data.iloc[:, [2]].values # dependent

# scaling
scaler = StandardScaler()
x = scaler.fit_transform(x)

# label_encodeing
label_encoder = preprocessing.LabelEncoder()
y = label_encoder.fit_transform(y)

# splitting the dataset
x_train, x_test, y_train, y_test = train_test_split(x,y,random_state=7,test_size=0.2)

# Building the model
dtc = DecisionTreeClassifier()
dtc.fit(x_train, y_train)

# making predictions
predictions = dtc.predict(x_test)

# accuracy and classification report
acc = accuracy_score(predictions, y_test)
report = classification_report(predictions, y_test)
print("Accuracy Score ", acc)
print("Classification Report")
print(report)

# Question 4: Regression with scikit-learn
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Create a dummy dataset
data = pd.DataFrame({
    'Bedrooms': [2, 3, 2, 4, 3, 3, 4, 2, 5, 4],
    'Square Footage': [1200, 1500, 1300, 2000, 1800, 1600, 2200, 1100, 2500, 2100],
    'Price':[150, 200, 180, 250, 220, 210, 280, 140, 320, 290]
})

# Selecting independet and dependent values
x = data.iloc[:, [0,1]].values # independent
y = data.iloc[:, [2]].values # dependent


# scaling
scaler = StandardScaler()
x = scaler.fit_transform(x)
y = scaler.fit_transform(y)

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x,y,random_state=7,test_size=0.2)

# Build a regression model (e.g., Linear Regression) Train the model on the training data
reg = LinearRegression()
reg.fit(x_train, y_train)

# making predictions
predictions = reg.predict(x_test)

# Evaluate the model's performance using mean squared error and R-squared
mean_square = mean_squared_error(predictions, y_test)
r_square = r2_score(predictions, y_test)
print(mean_square)
print(r_square)

# Question 6: Time Series Forecasting
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Create a dummy dataset
data = pd.DataFrame({
    'Date' : ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
    'Stock Price' : [100, 105, 110, 108, 115]
})

# converting the 'Date' column to datetime and set it as the index
data['Date'] = pd.to_datetime(data['Date'])
data.set_index(data['Date'], drop=False, append=False, inplace=False, verify_integrity=False).drop('Date', 1)

x = data['Date'].values
y = data['Stock Price'].values


label_encoder = preprocessing.LabelEncoder()
x = label_encoder.fit_transform(x)
x = x.reshape(x.shape[0], 1)

x_train, x_test, y_train, y_test = train_test_split(x,y,random_state=7,test_size=0.2)

# Build a regression model (e.g., Linear Regression) Train the model on the training data
reg = LinearRegression()
reg.fit(x_train, y_train)

# making predictions
predictions = reg.predict(x_test)

# Evaluate the model's performance using mean squared error and R-squared
mean_square = mean_squared_error(predictions, y_test)
r_square = r2_score(predictions, y_test)
print(mean_square)
print(r_square)

"""# Numpy and Pandas
* Q1. Ans - A) [5,7,9]
* Q2. Ans -	B) [2,4]
* Q3. Ans -	‘Bob’
* Q4. Ans -	4.414
* Q5. Ans -	A) [10, 40, 90, 160, 250]
* Q6. Ans -	A) [5, 7, 9]
* Q7. Ans -	‘Bob’
* Q8. Ans -	A) [1, 2, 3, 4, 5, 6, 9]
* Q9. Ans -	B)  [6, 15]
* Q10. Ans - C) 4.0

# Programming Questions
"""

# Que.1
import pandas as pd
data = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 30},
    {'name': 'Charlie', 'age': 22}
]

df = pd.DataFrame(data)

# printing the data
print("DataFrame:")
print(df)

# printing alice age
alice_age = df[df['name'] == 'Alice']['age'].values[0]
print("\nAge of Alice:", alice_age)

# printing average age
average_age = df['age'].mean()
print("\nAverage Age of All Individuals:", average_age)

# Que.2
import pandas as pd

data = {
    "City": ["New York", "Los Angeles", "Chicago"],
    "Population": [8623000, 3999759, 2716000]
}

df = pd.DataFrame(data)

# printing the dataframe
print("DataFrame:")
print(df)

# printing city with largest population
print("The city with the largest population is: ",df['City'][df['Population'].idxmax()] )


# calculating total population
print("The total population of all cities is: ", df['Population'].sum())

# Que.3
import numpy as np
arr = np.random.rand(20)
mean = np.mean(arr)
count_greater_than_0_5 = np.sum(arr > 0.5)

# printing the array
print("Array:", arr)

# printing the mean
print("Mean:", mean)

# counting values greater the 0.5
print("Count of values greater than 0.5:", count_greater_than_0_5)

#  Ques 4
data = {'ProductId' : [101, 102, 103], 'ProductName':['Laptop', 'Smartphone', 'Tablet'], "Price": [800, 400, 250]}
df = pd.DataFrame(data)

# printing the dataframe
print(df)

# printing the highest price
print("Max Price: ",df['Price'].max())

# printing cost of all product
print("Total Price:",df['Price'].sum())

# Ques 5
data = {'City' : ['London', 'Paris', 'Berlin'], 'Population':[8787892, 2206488, 3644826], "Area": [607, 40.7, 344]}
df = pd.DataFrame(data)

# printing the dataframe
print(df)

# printing highest population density
print("Highest Population Density: ", df['City'][(df['Population']/df['Area']).idxmax()])

# total area of all cities
print("Total Area of all cities: ", df['Area'].sum())