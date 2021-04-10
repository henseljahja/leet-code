from typing import List

class Solution:
    def numberOfSteps(self, num: int) -> int:
        x = bin(num).replace('0b','')
        cnt = 0
        p = len([i for i in x if i=='0'])
        q = len([i for i in x if i=='1'])*2
        return p+q-1
