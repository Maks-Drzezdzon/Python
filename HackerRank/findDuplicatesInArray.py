# 99.73%
from collections import Counter
class Solution:
    def findDuplicates(self, numbers: list[int]) -> list[int]:
        nums = Counter(numbers).items()
        return [k for k,v in nums if v>=2]
            