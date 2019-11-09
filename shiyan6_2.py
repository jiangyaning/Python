'''
编写人员类（Person），该类具有姓名（Name）、年龄（Age）、性别（Sex）等属性，
通过对Person类的继承得到教师类（Teacher），该类能够存放教师的职称、学历、工资、奖金等信息，并能计算出总收入（工资+奖金）。
'''
class Person:
    def __init__(self,Name,Age,Sex):
        self.Name=Name
        self.Age=Age
        self.Sex=Sex
        print ("姓名：%s\n年龄：%d\n性别：%s"%(self.Name,self.Age,self.Sex))
class Teacher(Person):
    def __init__(self,Name,Age,Sex,zhicheng,xueli,gonzi,jiangjin):
        Person.__init__(self,Name,Age,Sex)
        self.zhicheng=zhicheng
        self.xueli=xueli
        self.gonzi=gonzi
        self.jiangjin=jiangjin
        print ("职称：%s\n学历:%s\n工资:%d\n奖金:%d\n总收入:%d"%(self.zhicheng,self.xueli,self.gonzi,self.jiangjin,(self.gonzi+self.jiangjin)))
t=Teacher('李明',30,'男','教授','博士',5500,2000)


