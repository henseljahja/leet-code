from typing import List

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        x = [stones for stones in jewels]
        counter = 0
        for i in x:
            counter += stones.count(i)
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
    # t4 = list(map(int, input().strip('[]').split(',')))
    # t5 = int(input())
    t6 = list(input().strip('"'))
    t7 = list(input().strip('"'))
    print(s.numJewelsInStones(t6,t7))


if __name__ == "__main__":
    main()            
