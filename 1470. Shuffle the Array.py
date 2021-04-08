from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        xlen = int(len(nums)/2)
        x = nums[:xlen]
        y = nums[xlen:]
        out = []
        for i in range(xlen):
            out.append(x[i])
            out.append(y[i])
        return out

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
    t5 = int(input())
    print(s.shuffle(t4,t5))


if __name__ == "__main__":
    main()            
