year=int(input("请输入年份："))
if (year % 4 == 0) & (year % 100 != 0):
    print("%d年是闰年" % year)
elif year % 400 == 0:
    print("'%d'年是闰年" % year)
else:
    print("'%d'不年是闰年" % year)