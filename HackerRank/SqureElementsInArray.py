class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted([ele*ele for ele in A])