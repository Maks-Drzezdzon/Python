#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the isBalanced function below.
def isBalanced(s: str) -> str:
    stack = []
    for ele in s:
        if ele == '(' or ele == '[' or ele == '{':
            stack.append(ele)
        elif len(stack) == 0:
            return "NO"
        else:
            bracket = stack.pop()
            if bracket == '(' and ele != ')':
                return "NO"
            if bracket == '[' and ele != ']':
                return "NO"
            if bracket == '{' and ele != '}':
                return "NO"

    if len(stack) == 0:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
