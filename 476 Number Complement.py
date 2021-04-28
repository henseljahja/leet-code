class Solution:
    def findComplement(self, num: int) -> int:
        binNum = list(bin(num))[2:]
        binRep=""
        for i in binNum:
            if i == '0':
                binRep += "1"
            elif i == '1':
                binRep += "0"
        
        return int(binRep,2)
