"""
掷骰子决定做什么事情

"""

from random import randint
a=int(input("输入1开始掷色子:"))
if a==1:
    face = randint(1, 6)
if face == 1:
	result = '唱首歌'
elif face == 2:
	result = '跳个舞'
elif face == 3:
	result = '学狗叫'
elif face == 4:
	result = '做俯卧撑'
elif face == 5:
	result = '念绕口令'
else:
	result = '讲冷笑话'
print('你得到的数是%d,要做的事是：%s' % (face,result))


    

