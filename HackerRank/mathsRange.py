
def solution(A, B):
    # write your code in Python 3.6
    counter=0
    for ele in range(A, B +1):
        result = math(ele)
        if result == ele:
            counter +=1
        
    '''
    for ele in range(A + 1):
        s = math(ele)
        if s == A:
            counter_a += 1
        
    for ele in range(B + 1):
        s = math(ele)
        if s == B:
            counter_b += 1'''
    
    return counter

def math(number):
    return number * (number + 1)

print(solution(6,20))