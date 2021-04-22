class Solution:
    def findLucky(self, arr: List[int]) -> int:
        setArr = set(arr)
        res = []
        for i in setArr:
            res.append(arr.count(i))
        resZip = list(zip(setArr,res))
        for x,y in resZip[::-1]:
            if x ==y :
                return x
                break
        return -1
            
