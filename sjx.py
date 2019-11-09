import math
def pd(s):
    if s<=0:
        s = float(input("输入错误，请重新输入："))
        pd(s)
    return s
a = float(input("请输入三角形的边长a："))
a=pd(a)
b = float(input("请输入三角形的边长b："))
b=pd(b)
c = float(input("请输入三角形的边长c："))
c=pd(c)
if a+b<=c or a+c<=b or b+c<=a:
    print("a,b,c不能构成三角形！")
else:
    h = (a + b + c) / 2                #三角形周长的一半
    area = math.sqrt(h*(h-a)*(h-b)*(h-c));#三角形面积
    print(str.format("三角形三边分别为：a={0},b={1},c={2}", a, b, c))
    print(str.format("三角形的面积 = {0}", area))
