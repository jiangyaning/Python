
def abs(x, y):
    if x-y>=0:
        return x-y
    else:
        return y-x

x1,y1=eval(input("输入A点坐标，以逗号分隔："))
x2,y2=eval(input("输入B点坐标，以逗号分隔："))
mht=abs(x1,x2)+abs(y1,y2)
print("A(%.1f,%.1f),B(%.1f,%.1f)两点的的曼哈顿距离为：%.1f"%(x1,x2,y1,y2,mht))
