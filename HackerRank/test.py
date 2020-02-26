# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

#Given A, B, C, find any string of maximum length that can be created such that no 3 consecutive characters are same.
#There can be at max A 'a', B 'b' and C 'c'.


def solution(A, K):
    '''
    check if A is in range of 1 to K
    '''
    
    n = len(A)
    for i in range(n - 1):
        if (A[i] != A[i + 1] and A[i] + 1 == A[i + 1] - 1):
        # if (A[i] + 1 > A[i + 1]):
            return False
    if set(A) in set([ele for ele in range(1,K + 1)]):
    # if A[0] != 1 and A[n] != K:
        return False
    else:
        return True

'''  
print(solution([1,1,2,3], 3)) # true
print(solution([1,2,3], 3)) # true
print(solution([1,1,3], 2)) # false
print(solution([1,2,2,4], 4)) # false
print(solution([1,2,3,4], 4)) # true
'''



def idk(nums):
    '''
    this is kind of what i should have done for my interview but not really because it returns true or false instead of the number

    array is meant to look like
    [1,2,1,3,1,4]
    or
    [2,1,3,2,5,1]
    if it does not
    can you make it fit that pattern
    if so
    which num will you remove
    '''
    
    if len(nums) <= 1:
        return True
    
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            break
            
    a, b = nums[:], nums[:]
    
    a[i], b[i+1] = nums[i+1], nums[i]
    return a == sorted(a) or b == sorted(b)



#import re
from collections import Counter
def solution3(a, b, c):
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
# print(s([3,2,1,1],[6,2,3,4]))

# amazon
def selectPackages(truckSpace, packagesSpace):
    answer = dict()
    space_available = truckSpace - 30 # has to have 30 space left for safety reasons 
    
    for key, value in enumerate(packagesSpace):
        if space_available - value in answer:
            return [answer[space_available - value], key]
        
        answer[value] = key
            

# print(selectPackages(80,[40,30,20,10]))
# print(selectPackages(90,[30,30]))     


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

# amz
# string , k max letters
def substringk(s, k):
    if not s or k == 0:
        return []
    
    letter, res = {}, set()
    start = 0
    for i in range(len(s)):
        if s[i] in letter and letter[s[i]] >= start:
            start = letter[s[i]]+1
        letter[s[i]] = i
        if i-start+1 == k:
            res.add(s[start:i+1])
            start += 1
    return list(res)

# swvre 
# Flatten an array, e.g. [1,2,[3,4],5,[6,[8,9],10],11] -> [1,2,3,4,5,6,7,8,9,10,11]  
l=[1, 2, [3,4], 5, [6, [8,9], 10], 11, [12, 13, [14, [15, 16] ] ] ]
l2= [1,2,[3,4],5,[6,[8,9],10],11]

def convert(lis):
    a=[]   
    for ele in lis:
        if type(ele) is list:
            a.extend(convert(ele))
        else:
            a.append(ele)   
    return a 

# print(convert(l2))
#print(convert(l))

# amazon pretest
a = [1,0,0,0,1,0,0]
days = 1
result = [0,1,0,1,0,1,0]
def cells(a, days):
    pass


################################
# https://leetcode.com/discuss/interview-question/436073/
# https://leetcode.com/discuss/interview-question/414085/
# https://leetcode.com/problems/copy-list-with-random-pointer/