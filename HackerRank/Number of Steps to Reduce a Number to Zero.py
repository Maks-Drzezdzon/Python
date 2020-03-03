# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/  96.31%
class Solution:
    def numberOfSteps (self, num: int) -> int:
        answer = 0
             
        while num:
            if num % 2 == 0:
                num /= 2
                answer += 1
            else:
                num -= 1
                answer += 1
            
        return answer