class Solution:
    def minOperations(self, logs: List[str]) -> int:
        cnt = 0
        for i in logs:
            if i == "../":
                if cnt >0:
                    cnt -= 1
                else:
                    continue
            elif i == "./":
                continue
            else:
                cnt+=1
        # if cnt <0:
        #     cnt = 0
        return cnt
