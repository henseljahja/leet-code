from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(map(sum, accounts))

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
    t3 = cusIn(input())
    print(s.maximumWealth(t3))


if __name__ == "__main__":
    main()            
