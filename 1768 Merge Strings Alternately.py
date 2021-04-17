class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        mergedString = []
        for i in range(min(len(word1),len(word2))):
            mergedString.append(word1[i])
            mergedString.append(word2[i])
        if len(word1) > len(word2):
            mergedString.append(word1[i+1:])
        else:
            mergedString.append(word2[i+1:])
        return ''.join(mergedString)
