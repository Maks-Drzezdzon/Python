import tensorflow as tf
import keras
import pandas as pd
import numpy as np
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

x_train, y_train, x_test, y_test = sklearn.model_selection.train_test_split(x, y, test_size = 0.1)



