from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
    	out = []
    	c = 0
    	for i in nums:
    		c += i
    		out.append(c)
    	return out


def main():
    
    #Test Case
    s = Solution()
    # t1 = input()
    t2 = list(map(int, input().split(',')))
    # t3 = 

    print(s.runningSum(t2))


if __name__ == "__main__":
    main()            