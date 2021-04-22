class Solution:
    def reformatDate(self, date: str) -> str:
        lstDate = date.split(" ")
        month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        lstMonth = list(enumerate(month))
        
        getDate = ""
        if len(lstDate[0]) == 4:
            getDate = str(lstDate[0][:2])
        if len(lstDate[0]) == 3:
            getDate = "0"+str(lstDate[0][:1])
        
        getMonth = ""
        for i in range(len(lstMonth)):
            if lstMonth[i][1] == lstDate[1]:
                if lstMonth[i][0] >8:
                    getMonth = str(1+lstMonth[i][0])
                else: getMonth = "0"+str(1+lstMonth[i][0])
        
        getYear = str(lstDate[2])
        
        return ""+getYear+"-"+getMonth+"-"+getDate
        
