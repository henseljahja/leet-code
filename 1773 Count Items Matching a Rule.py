class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        rule = {"type" : 0, "color":1,"name":2}
        cnt = 0
        for i in range(len(items)):
            if items[i][rule[ruleKey]] == ruleValue:
               cnt +=1
        return cnt