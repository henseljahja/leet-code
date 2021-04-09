from typing import List

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = [first]
        for i in encoded:
            arr.append(arr[-1]^i)
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
    t2 = int(input())
    # t3 = cusIn(input())
    # t4 = list(map(int, input().strip('[]').split(',')))
    # t5 = int(input())
    # t6 = list(input().strip('"'))
    # t7 = list(input().strip('"'))
    # t8 = input().strip('"')

    print(s.decode(t1,t2))


if __name__ == "__main__":
    main()            
