from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = 0 
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    counter+=1
        return counter


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
    # t1 = list(map(int, input().strip('[]').split(',')))
    # t2 = int(input())
    # t3 = cusIn(input())
    t4 = list(map(int, input().strip('[]').split(',')))
    # t5 = int(input())
    print(s.numIdenticalPairs(t4))


if __name__ == "__main__":
    main()            
