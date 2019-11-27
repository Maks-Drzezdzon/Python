# https://leetcode.com/problems/two-sum/submissions/

def twoSum(num, target):
    answer = dict()
    
    for key, val in enumerate(num):
        if target - val in answer:
            return [answer[target - val], key]
        
        answer[val] = key


            
    '''
    dict[key] = [value]
    '''
    
    '''
    for ele in range(len(packages)):
        tmp = packages[ele - 1]
        package = packages[ele - 2]
        
        if tmp + package == target:
            answer.append(num.index(package))
            answer.append(num.index(tmp))
            return answer
        else:
            pass
    '''
            
print(twoSum([2,2], 4))
print(twoSum([1,2,3,4,5,6,7], 4))
print(twoSum([5,2,1,4,2,3], 8))
print(twoSum([9,8,4,2,3,4,1,2,3], 10))