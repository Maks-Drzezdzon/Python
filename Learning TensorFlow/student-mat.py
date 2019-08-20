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


# cant test model with used data
# this prevents poor results from being produced
# reserves 10% of data for testing
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split( x, y, test_size = 0.1)

l = linear_model.LinearRegression()
l.fit(x_train, y_train)
accuracy = l.score(x_test, y_test)
# print(accuracy) 88.6% accurate
# print('coefficient: ', l.coef_)
# print('intercept ', l.intercept_)

predict = l.predict(x_test)

for ele in range(len(predict)):
    print ('p ', predict[ele])
    print('x ', x_test[ele])
    print('y ', y_test[ele])

