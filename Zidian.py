snos=['17102','17101','17121','17119']
names=['蒋延平','黄承幸','周强','黄一烊']
scores=[90,92,98,93]
jyp=[]
for j in range(len(names)):
    jyp.append({'sno':snos[j],'name':names[j],'score':scores[j]})
i=input("请输入您要查找的姓名：")
if i=='蒋延平':
    print('查询结果如下：\n',jyp[0])
elif i=='黄承幸':
     print('查询结果如下：\n',jyp[1])
elif i=='周强':
    print('查询结果如下：\n',jyp[2])
elif i=='黄一烊':
    print('查询结果如下：\n',jyp[3])
else:
    print("对不起，查无此人！")