class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        cityA = []
        cityB = []
        
        for x,y in paths:
            cityA.append(x)
            cityB.append(y)
        return [x for x in cityB if x not in cityA][0]
