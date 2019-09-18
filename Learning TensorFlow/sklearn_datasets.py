import sklearn
from sklearn import datasets
from sklearn import svm
import pandas
import matplotlib


cancer = datasets.load_breast_cancer()

# print(cancer.feature_names)
# print(cancer.target_names)

x = cancer.data
y = cancer.target

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size = 0.1)

classes_name = ['malignant', 'benign']

# support vector machine
# create hyperplane splits data