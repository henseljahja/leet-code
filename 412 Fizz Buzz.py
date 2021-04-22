class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        fbList = []
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 == 0:
                fbList.append("FizzBuzz")
            elif i % 3 == 0:
                fbList.append("Fizz")
            elif i % 5 == 0:
                fbList.append("Buzz")
            else:
                fbList.append(str(i))
        return fbList
