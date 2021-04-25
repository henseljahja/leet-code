class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        evenList = [ x for x in nums if x%2==0]
        oddList = [ x for x in nums if x%2==1]
        resList = []
        for i in range(len(evenList)):
            resList.append(evenList[i])
            resList.append(oddList[i])
        return resList
