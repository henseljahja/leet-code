from typing import List

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        x = list(s)
        cnt,res = 0,0
        for i in x:
            if i =="R":
                cnt+=1
            elif i =="L":
                cnt-=1
            if cnt == 0:
                res+=1
            
        return res

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
    # t1 = list(map(int, input().strip('[]').split(',')))
    # t2 = int(input())
    # t3 = cusIn(input())
    # t4 = list(map(int, input().strip('[]').split(',')))
    # t5 = int(input())
    # t6 = list(input().strip('"'))
    # t7 = list(input().strip('"'))
    # t8 = input().strip('"')

    print(s.balancedStringSplit(t0))


if __name__ == "__main__":
    main()            
