from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        x = max(candies) - extraCandies
        return [i >= x for i in candies]

def main():
    
    #Test Case
    s = Solution()
    t1 = list(map(int, input().strip('[]').split(',')))
    t2 = int(input())
    # t3 = 

    print(s.kidsWithCandies(t1,t2))


if __name__ == "__main__":
    main()            
