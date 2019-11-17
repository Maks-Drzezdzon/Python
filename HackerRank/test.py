# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

#Given A, B, C, find any string of maximum length that can be created such that no 3 consecutive characters are same.
#There can be at max A 'a', B 'b' and C 'c'.

#import re
from collections import Counter
def solution(a, b, c):
    v = a+b+c
    answer = [None] * v
    counter = Counter(dict(a=a, b=b, c=c))
    
    for ele in range(v):
        for key, val in counter.most_common():
            if val > 0 and answer[ele - 2:ele + 1].count(key) < 2:
                answer[ele] = key
                counter[key] -= 1
                break
        else:
            return ''.join([ele for ele in answer if ele != None])
            
    # if re.findall(r'((\w)\2{2,})', answer):
        # return "wrong answer" no longer needed
    return ''.join(answer)
        


def s(A, B):

    A.sort()
    B.sort()
    i = 1
    for a in sorted(set(A)):
        if i < len(B) and B[i] < a:
            i += 1
        if a == B[i]:
            return a

    return -1




    
