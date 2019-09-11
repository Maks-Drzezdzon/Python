# working with irregular data
import pandas as pd
import sklearn
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from sklearn import linear_model, preprocessing

# note pandas reads in the first line of your data file as the col

data = pd.read_csv('car.data')
print(data.head())

# take lables and encode to int so 
# operation can be performed 
pe = preprocessing.LabelEncoder()

# mapping data to col name to convert
buying = pe.fit_transform(list(data["buying"]))
maint = pe.fit_transform(list(data["maint"]))
lug_boot = pe.fit_transform(list(data["lug_boot"]))
safety = pe.fit_transform(list(data["safety"]))
clas = pe.fit_transform(list(data["class"]))

