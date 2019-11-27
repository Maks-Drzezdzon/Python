# https://leetcode.com/problems/spiral-matrix-ii/
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        row = col = count = 0
        size = n-1
        A = [[None for _ in range(n)] for _ in range(n)]
        
        for ith_num in range(1, n**2 + 1):
            if A[row][col]:
                row += 1; col += 1;
                count += 1; size -= 1
                
            A[row][col] = ith_num
            
            if row == count and col < size: col += 1
            elif row < size and col == size : row += 1
            elif row == size and col > count : col -= 1
            elif row > count and col == count: row -= 1
                
        return A