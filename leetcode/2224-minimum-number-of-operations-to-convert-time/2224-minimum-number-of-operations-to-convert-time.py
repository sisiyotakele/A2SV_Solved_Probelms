class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        ch, cm = map(int, current.split(':'))
        th, tm = map(int, correct.split(':'))
        
        diff = (th * 60 + tm) - (ch * 60 + cm)
        
        ops = 0
        for step in [60, 15, 5, 1]:
            ops += diff // step
            diff %= step
        
        return ops