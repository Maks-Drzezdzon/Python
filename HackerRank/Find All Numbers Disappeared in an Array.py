class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        setA = set(nums)
        setB = set([ele for ele in range(1, len(nums) + 1)])
        return setB.difference(setA)
    
    '''
        setB = set()
        for ele in range(1, len(nums) + 1):
            if ele not in set(nums):
                setB.add(ele)
        return setB
        # return [ele for ele in range(1, len(nums) + 1) if ele not in set(nums)]
    '''