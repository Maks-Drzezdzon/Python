# https://leetcode.com/problems/sort-array-by-parity/submissions/ 99.13%
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        return list([even for even in A if even % 2 == 0] + [odd for odd in A if odd % 2 !=0])