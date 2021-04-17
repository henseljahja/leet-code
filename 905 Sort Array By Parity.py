class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        evenList = []
        oddList = []
        for i in A:
            if i % 2 == 0:
                evenList.append(i)
            else:
                oddList.append(i)
        return evenList + oddList
            
            
