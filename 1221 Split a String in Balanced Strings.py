from typing import List

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        x = list(s)
        cnt,res = 0,0
        for i in x:
            if i =="R":
                cnt+=1
            elif i =="L":
                cnt-=1
            if cnt == 0:
                res+=1
            
        return res
