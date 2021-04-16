class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        x,y = list(coordinates)
        if ord(x) % 2 == 1:
            return int(y) % 2 == 0
        
        elif ord(x) % 2 == 0:
            return int(y) % 2 == 1
