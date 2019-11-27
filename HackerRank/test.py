# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

#Given A, B, C, find any string of maximum length that can be created such that no 3 consecutive characters are same.
#There can be at max A 'a', B 'b' and C 'c'.

#import re
# liberty IT
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

# amazon
def selectPackages(truckSpace, packagesSpace):
    answer = dict()
    space_available = truckSpace - 30 # has to have 30 space left for safety reasons 
    
    for key, value in enumerate(packagesSpace):
        if space_available - value in answer:
            return [answer[space_available - value], key]
        
        answer[value] = key
            

print(selectPackages(80,[40,30,20,10]))
print(selectPackages(90,[30,30]))     


def retrieveMostFrequentlyUsedWords(literatureText, wordsToExclude):
    literature = list(literatureText.split(" "))
    exclude = list(wordsToExclude)
    print("text " + str(literature))
    print("exclude " + str(exclude))
    answer=[]

    for word in literature:
        if word in exclude:
            pass
        else:
            answer.append(word)
    
    return answer

text = "rose is a flower rose is pond a flower rose flower in garden garden garden pond pond rose is a rose is a rose is a rose is a"
words = ["a","rose","is"]
#print(retrieveMostFrequentlyUsedWords(text, words))


# swvre 
# Flatten an array, e.g. [1,2,[3,4],5,[6,[8,9],10],11] -> [1,2,3,4,5,6,7,8,9,10,11]  
l=[1,2,[3,4],5,[6,[8,9],10],11,[12,13,[14,[15,16]]]]
l2= [1,2,[3,4],5,[6,[8,9],10],11]

def convert(l):
    a=[]   
    for ele in l:
        if type(ele) is list:
            a.extend(convert(ele))
        else:
            a.append(ele)   
    return a 

#print(convert(l2))
#print(convert(l))
    
################################
# https://leetcode.com/discuss/interview-question/436073/
# https://leetcode.com/discuss/interview-question/414085/
# https://leetcode.com/problems/copy-list-with-random-pointer/