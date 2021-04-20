class Solution:
    def calPoints(self, ops: List[str]) -> int:
        sumOps = []
        for i in range(len(ops)):
            if ops[i] == '+':
                sumOps.append(int(sumOps[-2])+int(sumOps[-1]))
            elif ops[i] == 'D':
                sumOps.append(int(sumOps[-1])*2)
            elif ops[i] == 'C':
                # sumOps.pop(ops[i-1]))
                sumOps.pop()
            else:
                sumOps.append(int(ops[i]))
        return sum(sumOps)
