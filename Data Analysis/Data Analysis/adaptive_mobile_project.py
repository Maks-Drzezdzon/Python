import pandas as pd
import re
from detect_delimiter import detect

path = "../Data/adaptive_mobile_dataset.csv"

def read_file(path):
    data = pd.read_csv(path) 
    print(data)

# read_file(path)

def to_tsv(path):
    '''
    2) How would transform this file into a TSV file? (i.e. a file where the comma separator ',' is substituted with a tab character '\t')
    '''
    file = path.split('/')[-1]
    with open(file, 'r') as myfile:
      with open("test.txt", 'w') as csv_file:
        for line in myfile:
          # fileContent = re.sub("-", "\t", line)
          fileContent = re.sub(",", "\t", line)
          csv_file.write(fileContent)

def data_sample():
    '''
    3) How would you extract a random sample of 5% of the rows from this file?
    '''
    pass

def min_max_date_time():
    '''
    4) How would extract the minimum and maximum value from the "Datetime" column?
    '''
    pass

def no_duplicated_ids():
    '''
    5) Let us suppose we don't want duplicated "ID"s. In case there are rows 
   with duplicated IDs we just keep the first row we've found: how would you 
   extract a file, from the original one, without duplicated IDs?
    '''
    pass


def to_unix_timestamp():
    '''
    6) How would you create a new file where the "Datetime" column is substituted
    with a "Timestamp" column with the (Unix) timestamp in milliseconds?
    i.e., for the example above you would have:
    '''
    pass
   
    
def count_orderby():
    '''
    7) How would you create a simple count of the distinct "SourceType"s? 
    i.e. we want to see each distinct "SourceType", with the number
    of times it appears in the file, sorted by descending number of occurencies.
    '''
    pass


'''
Questions:
1) Which considerations can you make about the input data? 
    # i have no idea ? check it conforms to a pattern ?
    If the file size is big (let’s say 20GB), how would store it? 
    # it depends on what kind of data it is
    # compress it
    
    Would you keep the original format? If not, what would you do? 
    
    Could you describe different options/format for storing the data? 
    
    Which sanity checks would you apply and why?
'''