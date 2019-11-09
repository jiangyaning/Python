import os
a=input("请输入一个文件夹名：")
if os.path.exists(a):
    print("%s是一个文件"%a)
    print("该文件的信息如下：")
    print("文件大小：%d"%os.path.getsize(a))
    print("文件的路径:%s"%os.path.abspath(a))
    if os.path.isdir(a):
        print("%s是目录。"%a)
    if os.path.isfile(a):
        print("%s是普通文件"%a)
else:
    print("对不起，您输入的文件不存在！")