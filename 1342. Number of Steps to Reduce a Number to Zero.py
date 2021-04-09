from typing import List

class Solution:
    def numberOfSteps(self, num: int) -> int:
        x = bin(num).replace('0b','')
        cnt = 0
        p = len([i for i in x if i=='0'])
        q = len([i for i in x if i=='1'])*2
        return p+q-1

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
    t2 = int(input())
    # t3 = cusIn(input())
    # t4 = list(map(int, input().strip('[]').split(',')))
    # t5 = int(input())
    # t6 = list(input().strip('"'))
    # t7 = list(input().strip('"'))
    print(s.numberOfSteps(t2))


if __name__ == "__main__":
    main()            
