#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    rows = len(arr) -2
    cols = len(arr[0]) -2

    max_sum = -sys.maxsize -1 
    # this is how you do Intger.MIN_VALUE in python, do without - for max

    for row in range(rows):
        for col in range(cols):
            curren_sum =arr[row][col] +arr[row][col+1] +arr[row][col+2]+arr[row+1][col+1]+arr[row+2][col] +arr[row+2][col+1] +arr[row+2][col+2]
            max_sum = max(max_sum, curren_sum)
    
    return max_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
