from typing import List

class Solution:
    def defangIPaddr(self, address: str) -> str:
        #out = [] 
        #for i in address.split('.'):
        #    out.append(i)
        #    out.append('[.]')
        return address.replace(".","[.]")

def main():
    
    #Test Case
    s = Solution()
    t1 = input()
    # t2 = 
    # t3 = 

    print(s.defangIPaddr(address = t1))


if __name__ == "__main__":
    main()            