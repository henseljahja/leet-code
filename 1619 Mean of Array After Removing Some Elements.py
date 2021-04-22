class Solution:
    def trimMean(self, arr: List[int]) -> float:
        sortedArr = sorted(arr)
        bott5 = int(len(arr)*0.05)
        top5 = int(len(arr)*0.95)
        
        newArr = sortedArr[bott5:top5]
        
        return sum(newArr)/len(newArr)
