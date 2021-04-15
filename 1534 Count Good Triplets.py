class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        lenArr = len(arr)
        cnt = 0 
        for i in range(lenArr-2):
            for j in range(i+1,lenArr-1):
                for k in range(j+1,lenArr):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j]-arr[k])<=b and abs(arr[i] - arr[k])<=c:
                        cnt+=1
        return cnt
