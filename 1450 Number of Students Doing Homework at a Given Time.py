class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        cnt = 0
        for i in range(len(endTime)):
            workTime = [x for x in range(startTime[i],endTime[i]+1)]
            if queryTime in workTime:
                cnt+=1
        return cnt
