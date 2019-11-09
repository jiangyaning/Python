class Student:   #学生类
     count=0
     def __init__(self, sno,name, sex,age):#构造函数
            self.sno=sno
            self.name=name
            self.sex=sex
            self.age=age
            Student.count+=1
     def printMsg(self):#显示学生信息
            return print("%s    %s   %s   %d"%(self.sno,self.name,self.sex,self.age))
stu=[[201706401101,"张三","男",19],[201706401102,"李四","女",20],[201706401103,"王五","女",20],[201706401104,"马六","男",21]]#学生列表
s=[]
for i in range(len(stu)):
    s.append(Student(stu[i][0],stu[i][1],stu[i][2],stu[i][3]))
print("实例化了%d个学生,信息如下："%Student.count)
print("学号            姓名   性别  年龄")
for sl in s:
    sl.printMsg()



