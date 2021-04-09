from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        arr = list(zip(indices,s))
        arr.sort()
        p,q = zip(*arr)
        return ''.join(q)

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
    t0 = list(input().strip('"'))
    t1 = list(map(int, input().strip('[]').split(',')))
    # t2 = int(input())
    # t3 = cusIn(input())
    # t4 = list(map(int, input().strip('[]').split(',')))
    # t5 = int(input())
    # t6 = list(input().strip('"'))
    # t7 = list(input().strip('"'))
    print(s.restoreString(t0,t1))


if __name__ == "__main__":
    main()            
