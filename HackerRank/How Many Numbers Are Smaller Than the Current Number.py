class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        a = sorted(nums)
        answer = [a.index(ele) for ele in nums]
               
        return answer