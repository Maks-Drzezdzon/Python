import pandas as pd
import re


reviews_dataset_path = "../Data/reviews.csv"
reviews_dataset = pd.read_csv(reviews_dataset_path, error_bad_lines=False, lineterminator='\n')
reviews_dataset.columns = ['A', 'B', 'C', 'D' , 'E', 'F']

t = reviews_dataset.drop_duplicates(subset='A', keep="first", inplace=True)
print(t)