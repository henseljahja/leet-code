class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sortedNums = sorted(nums)
        maxSum = 0
        for i in range(0,len(sortedNums)-1,2):
            maxSum = maxSum + min(sortedNums[i],sortedNums[i+1])
        return maxSum
