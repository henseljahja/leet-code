class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        largestSquares = []
        for i in rectangles:
            x,y = i
            largestSquares.append(min(x,y))
        maxSquares = max(largestSquares)
        return largestSquares.count(maxSquares)
