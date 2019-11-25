
def searchMatrix(matrix, target) -> bool:
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    if not matrix and matrix[0]:
        return False
    
    i, j=0, len(matrix[0]) - 1
    while i < len(matrix) and j > -1:
        if matrix[i][j] == target:
            return True
        elif matrix[i][j] < target:
            i += 1
        else:
            j -= 1
    
    return False
        
    
m=[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]


target = 5
print(searchMatrix(m,target))

