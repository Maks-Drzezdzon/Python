import math
import os
import random
import re
import sys
from collections import Counter
# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    answer = Counter(note) - Counter(magazine)
    
    if bool(answer):
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
