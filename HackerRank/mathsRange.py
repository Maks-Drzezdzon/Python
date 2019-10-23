def solution(A, B):
    '''
    this was meant to take a range of elements i.e 6 - 20 inclusive
    and return if any, pairs of numbers that conform with formula of
    N * ( N + 1)
    
    in range 6,20
    6=2*3, 12=3*4, 20=4*5
    
    and return how many pairs can be made
    
    '''
    counter=0
    
    for ele in range(A, B + 1):
        result = math_helper_function(ele)
        if result == 1:
            counter +=1
        else:
            pass
 
    return counter

def math_helper_function(numbers):
    for number in range(numbers + 1):
        result = number * (number + 1)
        if result == numbers:
            return 1
        else:
            pass

# test cases
print(solution(6,20))