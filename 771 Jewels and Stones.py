from typing import List

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        x = [stones for stones in jewels]
        counter = 0
        for i in x:
            counter += stones.count(i)
        return counter
