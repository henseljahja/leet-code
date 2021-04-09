from typing import List

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        arr = []
        for i in range(0,len(nums)-1,2):
            for j in range(nums[i]):
                arr.append(nums[i+1])
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
    # t4 = list(map(int, input().strip('[]').split(',')))
    # t5 = int(input())
    # t6 = list(input().strip('"'))
    # t7 = list(input().strip('"'))
    print(s.decompressRLElist(t1))


if __name__ == "__main__":
    main()            
