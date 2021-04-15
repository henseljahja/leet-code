class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        lenSplit = int(len(s)/2)
        s = list(s.lower())
        left = s[lenSplit:]
        right = s[:lenSplit]
        vowel = ['a', 'e', 'i', 'o', 'u']
        cntRight, cntLeft = 0,0
        for i in range(lenSplit):
            if left[i] in vowel:
                cntLeft+=1
            if right[i] in vowel:
                cntRight+=1
        return cntLeft == cntRight
            
            
