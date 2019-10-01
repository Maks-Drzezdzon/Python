from collections import Counter
# https://leetcode.com/problems/unique-number-of-occurrences/ 87.75%
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = dict(Counter(arr))
        s = set()
        
        for ele in d.values():           
            s.add(ele)
        if len(s) == len(d.keys()):
            return True
    
        return False
    ''' or 
        d = dict(Counter(arr))
        return len(d) == len(set(d.values()))
    '''