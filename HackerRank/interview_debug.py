def solution(A, K):
    '''
    debug the following you can only change two lines of code to make it work
    this solution isnt finished its the original
    
    def takes an array of n ints
    and k the range
    
    this function should say true if
    elements are in range of k
    false if
    elements are not in rage of k
    '''
    n = len(A)
    
    for i in range(n - 1):
        if (A[i] + 1 < A[i + 1]):
            return False
        
    if (A[0] != 1 and A[n - 1] != K):
        return False
    
    else:
        return True
    
# test cases
print(solution([1, 1, 2, 3, 3], 3)) # true
print(solution([1, 1, 3] , 2)) # flase