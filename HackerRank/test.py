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


def selectPackages(truckSpace, packagesSpace):
    answer = list()
    space = 30
    
    for i in list(sorted(reversed(packagesSpace))):
        package1 = i
        package2 = i+1
        
        if truckSpace - (package1 + package2) >= 30:
            answer.append(package2)
            answer.append(package1)

    
    return answer
    

#print(selectPackages(80,[40,30,20,10]))   

from collections import Counter
def retrieveMostFrequentlyUsedWords(literatureText, wordsToExclude):
    literature = list(literatureText.split(" "))
    exclude = list(wordsToExclude)
    print(exclude)
    for word in exclude:
        if word in literature:
            print(literature.remove(word))
       
    print(literature)
    counter = Counter(literature)
    

    # im not sure why for case 2 it feels like the code isnt being run ?
    # the filer isnt taking out words
    
    return list(dict(counter.most_common(1)))

text = "rose is a flower rose is pond a flower rose flower in garden garden garden pond pond rose is a rose is a rose is a rose is a"
words=["a","rose","is"]
# print(retrieveMostFrequentlyUsedWords(text, words))