class Solution:
    def totalMoney(self, n: int) -> int:
        cnt = 0
        index = 1
        while n >= 7:
            cnt += sum([x for x in range(index,7+index)])
            n -= 7
            index += 1
        if n > 0:
            cnt+= sum([x for x in range(index,n+index)])
        return cnt
        
