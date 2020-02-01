import pandas as pd
import re


reviews_dataset_path = "../Data/reviews.csv"
reviews_dataset = pd.read_csv(reviews_dataset_path, error_bad_lines=False, lineterminator='\n')
print(reviews_dataset)
    