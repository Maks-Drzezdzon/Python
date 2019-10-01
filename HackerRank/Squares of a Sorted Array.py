# https://leetcode.com/problems/squares-of-a-sorted-array/submissions/ 96.85%
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted(list([ele*ele for ele in A]))