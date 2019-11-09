import keyword
z=tuple(keyword.kwlist)
#print(z)
i=input("请输入一个单词：")
if i in z:
    print(i,"是Python的一个关键字！")
else:
    print(i,"不是P ython的关键字!")