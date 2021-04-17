class Solution:
    def sumZero(self, n: int) -> List[int]:
        lenList = int(n/2)
        leftList = [-x for x in range(1,lenList+1)]
        rightList = [x for x in range(1,lenList+1)]
        if n % 2 == 0:
            return leftList+rightList
        else:
            return leftList+[0]+rightList
