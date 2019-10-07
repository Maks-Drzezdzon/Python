from collections import Counter
class Solution:
    def answer(a:list) -> int:
        
        b = dict(Counter(a))
        print(max(b,key=b.get))
        
        
        
        
    answer([1,3,5,2,1])
        