# working with irregular data
import pandas as pd
import sklearn
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from sklearn import linear_model, preprocessing

# KNN is a classification alg
# create groups
# data is then going to be put into closest groups ie neighbor
# set var to a nummber which will dictated the x closest points to your data point
# x closest points to var are of group A so var probably belongs to group A
# E.G x = 5, 2 are Group A 3 are Group B, var probably belongs to group B
# x has to be an odd number so there will always be an uneven split making 1 group dominant
# x should not be too high so that far off points dont get picked for small data groups
# KNN is comp heavy because distance is calc for each point every time


# note pandas reads in the first line of your data file as the col

data = pd.read_csv('car.data')
# print(data.head())

# take lables and encode to int so 
# operation can be performed 
pe = preprocessing.LabelEncoder()

# mapping data from col name to variables
buying = pe.fit_transform(list(data["buying"]))
maint = pe.fit_transform(list(data["maint"]))
door = pe.fit_transform(list(data["door"]))
persons = pe.fit_transform(list(data["persons"]))
lug_boot = pe.fit_transform(list(data["lug_boot"]))
safety = pe.fit_transform(list(data["safety"]))
clas = pe.fit_transform(list(data["class"]))
# print(buying)
predict = "class"

X = list(zip(buying, maint, door, persons, lug_boot, safety))
Y = list(clas)


x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, Y, test_size = 0.1)

# print(x_train, y_test)
