class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bn = bin(n)
        
        return '00' not in bn and '11' not in bn
