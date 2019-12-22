#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    # rows = len(arr) -2
    # cols = len(arr[0]) -2
    maxval = - sys.maxsize -1
    for row in range(len(arr) -2):
        for col in range(len(arr[0]) -2):
            
            hourglass = \
            arr[row][col] + arr[row][col+1] + arr[row][col+2] \
            + arr[row+1][col+1] + \
            arr[row+2][col] + arr[row+2][col+1] + arr[row+2][col+2] 
            
            maxval = max(maxval, hourglass)
    return maxval


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
