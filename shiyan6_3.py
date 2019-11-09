class groupScore:
    score=[]
    Total=0
    count=0
    def setScore(self):
        while groupScore.count<3:
            groupScore.count+=1
            groupScore.score.append(int(input("请输入第%d个同学的成绩："%groupScore.count)))
    def getScore(self):
      return groupScore.score
    def sum(self):
        for i in groupScore.getScore(self):
            groupScore.Total+=i
    def average(self):
        return groupScore.Total/groupScore.count
    def show(self):
        print("总分为:%d"%groupScore.Total)
        print("平均分为:%d"%groupScore.average(self))

s=groupScore()
s.setScore()
s.getScore()
s.sum()
s.average()
s.show()
