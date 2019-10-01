from collections import Counter
# https://leetcode.com/problems/unique-number-of-occurrences/
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = dict(Counter(arr))
        s = set()
        
        for ele in d.values():           
            s.add(ele)
        if len(s) == len(d.keys()):
            return True
        
        if len(s) < len(d.keys()):
            return False
        
        return False