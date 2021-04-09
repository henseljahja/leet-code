from typing import List

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = list(str(n))
        arr = [int(x) for x in s]
        SOD = sum(arr)
        POD = 1
        for i in arr:
            POD *= i
        return POD - SOD


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
    # t1 = list(map(int, input().strip('[]').split(',')))
    t2 = int(input())
    # t3 = cusIn(input())
    # t4 = list(map(int, input().strip('[]').split(',')))
    # t5 = int(input())
    # t6 = list(input().strip('"'))
    # t7 = list(input().strip('"'))
    print(s.subtractProductAndSum(t2))


if __name__ == "__main__":
    main()            
