from typing import List

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        arr = []
        for i in range(len(nums)):
            arr.insert(index[i],nums[i])
        return arr

def cusIn(inp):
    x = []
    lst = list(inp.strip('[]').split('],['))
    for i in lst:
        p = list(map(int, i.split(',')))
        x.append(p)
    return x

def main():
    
    #Test Case
    s = Solution()
    # t0 = list(input().strip('"'))
    t1 = list(map(int, input().strip('[]').split(',')))
    # t2 = int(input())
    # t3 = cusIn(input())
    t4 = list(map(int, input().strip('[]').split(',')))
    # t5 = int(input())
    # t6 = list(input().strip('"'))
    # t7 = list(input().strip('"'))
    # t8 = input().strip('"')

    print(s.createTargetArray(t1,t4))


if __name__ == "__main__":
    main()            
