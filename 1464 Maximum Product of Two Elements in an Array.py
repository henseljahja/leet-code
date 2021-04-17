class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxVal = 0
        lenNums = len(nums)
        
        for i in range(lenNums-1):
            for j in range(i+1,lenNums):
                con = (nums[i]-1) * (nums[j]-1)
                if con > maxVal:
                    maxVal = con
        return maxVal
