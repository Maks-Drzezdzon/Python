from functools import reduce
import operator

class Solution:
    def beautifulArray(self, N: int) -> List[int]:
        lst = [[ele for ele in range(1, N + 1)]]
        tmp = []
        
        # size of small list have odd and even in pairs
        while len(lst[0]) > 2:
            
            for l in lst:
                # hold even
                tmp.append([l[i] for i in range(0,len(l),2)])
                # hold odd
                tmp.append([l[i] for i in range(1,len(l),2)])
            # when its done copy and sort    
            lst = tmp.copy()
            tmp = []
            print(lst)
        return reduce(operator.add, lst)
        