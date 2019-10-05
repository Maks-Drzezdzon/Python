# https://leetcode.com/problems/robot-return-to-origin/submissions/ 99.95%
class Solution:
    def judgeCircle(self, moves):
        if moves.count("U")==moves.count("D") and moves.count("L")==moves.count("R"):
            return True
        return False