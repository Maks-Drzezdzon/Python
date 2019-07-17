import csv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import re

def main():
    data = pd.read_csv('log.csv')
    data['Address'] = data.Address.astype('str')
    # print(data.dtypes) 
    # open file for reading
   
    #https://pythex.org/
    #\W(103)
    
    def time():
        data = pd.read_csv('unique.csv')
        # prints out occurances over ip count     
        # data['Time'] = pd.to_datetime(data.Time)
        # works on the data sample using the occurances data as x value
        # sorts it by index to make the plot more smooth and plots it
        data.Occurrences.value_counts().sort_index().plot()
        # names labels x and y
        plt.xlabel('Number of occurrences')
        plt.ylabel('Unique addresses recorded')
        # plt.plot(sample.Occurrences , sample.Unique_IP)
    
        time()
    
    
    
    def heat():
        data = pd.read_csv('log.csv')
        data['Time'] = pd.to_datetime(data.Time)
        data.Time.value_counts().sort_index().plot()
        # prints out occurances over ip count     
        # group_a = data[data.Address] 
        # group_b = data[data.Address] 
        # group_c = data[data.Address]
        
        heat()
       
main()       




"""
x = []
y = []

with open('sorted_log.txt' , 'r') as cvsfile:
    plots = csv.reader(cvsfile , delimiter = ' ')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

#numpy
#x , y = np.loadtxt('sorted_log.txt' , delimiter = ' ' , unpack = True)


plt.plot(x ,y ,label='welp')  
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
"""