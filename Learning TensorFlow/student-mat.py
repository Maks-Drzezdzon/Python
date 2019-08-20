import tensorflow as tf
import keras
import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle


# ; is the seperator
data = pd.read_csv("student-mat.csv", sep = ";")
# print(data.head()) # looking at data
data = data[["G1","G2","G3","studytime","failures","absences"]]
# print(data.head())

# label is what you are trying to predict in this case its the final grade
label_grade = "G3"

x = np.array(data.drop([label_grade], 1))
y = np.array(data[label_grade])


# splits data into 10% for testing
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split( x, y, test_size = 0.1)

l = linear_model.LinearRegression()
l.fit(x_train, y_train)
accuracy = l.score(x_test, y_test)
# print(accuracy) 88.6% accurate



