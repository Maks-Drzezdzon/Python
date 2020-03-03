class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        tmp = [str(ele).replace('', ' ').split() for ele in nums if not None]
        answer = [ele for ele in [str(ele).replace('', ' ').split() for ele in nums if not None] if len(ele) % 2 == 0]
        return len(answer)