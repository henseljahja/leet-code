import importlib
import os,sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# mod = input()
solutionMod = __import__("1486 XOR Operation in an Array")

def main():
    
    #Test Case
    s = solutionMod.Solution()
    # t1 = list(map(int, input().strip('[]').split(',')))
    t2 = int(input())
    # t3 = cusIn(input())
    # t4 = list(map(int, input().strip('[]').split(',')))
    t5 = int(input())
    # t6 = list(input().strip('"'))
    # t7 = list(input().strip('"'))
    print(s.xorOperation(t2,t5))


if __name__ == "__main__":
    main()       