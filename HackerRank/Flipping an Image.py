# https://leetcode.com/problems/flipping-an-image/submissions/ 98.37
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        return list([[1 - ele for ele in List][::-1] for List in A])
        """or return [[ele ^ 1 for ele in List][::-1] for List in A] leet code doesnt seem to want to tell me which is quicker"""


        