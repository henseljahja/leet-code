class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        setNums = set(nums)
        cntUniqueElements = 0
        for i in setNums:
            if nums.count(i) == 1:
                cntUniqueElements+=i
        return cntUniqueElements

