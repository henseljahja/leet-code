class Solution:
    def maxDepth(self, s: str) -> int:
        cnt, mx = 0,0
        for i in s:
            if i == "(":
                cnt +=1
                if cnt > mx:
                    mx = cnt
            elif i == ")":
                cnt -=1
        return mx
