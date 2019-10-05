# https://leetcode.com/problems/height-checker/ 96.76%
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        srt = sorted(heights)
        move = 0
       
        for srt,ele in zip(srt, heights):
            if srt != ele:
                move += 1
        
        return move
    
    """ or 
            for ele in range(len(heights)):
                if srt[ele] == heights[ele]:
                    move += 1
        
        return len(srt) - move
        
        or 
        
            for ele in range(len(heights)):
                if srt[ele] != heights[ele]:
                    move += 1
        
        return move
    """