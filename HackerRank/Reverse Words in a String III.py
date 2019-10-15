# https://leetcode.com/problems/reverse-words-in-a-string-iii/submissions/ 97.95%
class Solution:
    def reverseWords(self, s: str) -> str:        
        return ' '.join([ele[::-1] for ele in s.split(' ')] )