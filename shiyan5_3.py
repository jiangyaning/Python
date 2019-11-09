def output_avg(L):#输出两门课的班级平均分
    sum1=sum2=0
    for i in range(4):
        sum1+=int(L[i][1])
        sum2+=int(L[i][2])
    print("这个班的数学平均分为：%4.1f，语文平均分为：%4.1f" % (sum1/4, sum2/4))
def output_notpass(L):#输出两门课均不及格的学生成绩信息
    for i in range(4):
        if int(L[i][1])<60 and int(L[i][2])<60:
            print("两门课均不及格的学生学号及数学、语文成绩为：\n{}".format(' '.join(L[i])))
def output_good(L):#输出两门课评均在90分以上的学生成绩信息
    print("两门课平均分在90分以上的学生学号及数学、语文成绩为：")
    for i in range(4):
        if (int(L[i][1])+int(L[i][2]))/2>90:
            print(' '.join(L[i]))
c=[]
f=open('data/class_score.txt')
for i in f.readlines():
    c.append(i.rstrip('\n').split())
f.close()
output_avg(c)
output_notpass(c)
output_good(c)




