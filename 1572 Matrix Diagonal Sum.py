class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        lenMat = len(mat)
        midMat = int(lenMat/2)
        
        cnt = 0
        
        for i in range(lenMat):
            cnt += mat[i][i]
            cnt += mat[lenMat-1-i][i]
            
        if lenMat % 2 == 1:
            cnt -= mat[midMat][midMat]
        
        return cnt
