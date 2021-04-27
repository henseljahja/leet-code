class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odd,even = 0,0
        for i in position:
            if i %2 ==0:
                even +=1
            elif i%2 ==1:
                odd +=1
        return min(odd,even)
