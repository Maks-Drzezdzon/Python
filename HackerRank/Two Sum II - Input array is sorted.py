# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

def twoSum(num, target):
    answer = dict()
    
    for key, val in enumerate(num, 1):
        if target - val in answer:
            return [answer[target - val], key]
        
        answer[val] = key