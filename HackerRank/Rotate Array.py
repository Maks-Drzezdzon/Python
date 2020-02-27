
def idk(nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        while k:
            nums.insert(0, nums.pop())
            k -= 1
        return nums

print(idk([1,2,3,4,5,6], 2))
print(idk([1,2,3,4,5,6], 4))
print(idk([1,2,3], 2))