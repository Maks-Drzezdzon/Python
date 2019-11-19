#  https://leetcode.com/problems/self-dividing-numbers/submissions/ 95.00

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        l=[]
        
        for ele in range(left, right+1):
            string = str(ele)
            str_len = len(string)
            count=0
            if '0' not in string:
                for number in string:

                    if ele % int(number) == 0:
                        count += 1
                    else:
                        break
                    if count == str_len:
                        l.append(ele)
                           
        return l
                             