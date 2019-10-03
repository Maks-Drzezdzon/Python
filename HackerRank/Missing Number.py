# https://leetcode.com/problems/missing-number/submissions/ 68.63%
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return set(range(len(nums)+1)).difference(set(nums)).pop()