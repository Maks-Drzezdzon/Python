def answer(target,nums):
    answer=dict()
    
    for key, value in enumerate(nums):
        if target - value in answer:
            return [answer[target - value], key]
        
        answer[value] = key
    
print(answer(2,[1,2,3,1, -1]))


def matrix(matrix, target):
    if not matrix and matrix[0]:
        return False
    
    i, j = 0, len(matrix[0]) - 1
    while i < len(matrix) and j > -1:
        if matrix[i][j] == target:
            return True
        elif matrix[i][j] < target:
            i += 1
        else:
            j -= 1


m=[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
print(matrix(m,6))