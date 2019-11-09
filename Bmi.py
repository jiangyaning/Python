x=input("您的姓名：")
s=float(input("身高（米）："))
t=float(input("体重（kg）："))
bmi=t/(s**2)
if bmi<18.5:
    print("您太瘦了，体重过轻，请加强营养！")
elif bmi<25:
    print("恭喜您，您的身材非常好！")
elif bmi<28:
    print("您的身材有点偏胖，请请努力回到以前的标准身材！")
elif bmi<32:
    print("您是一个小胖子，请注意饮食和加强锻炼！")
else:
    print("您严重肥胖，肥胖不好哟，要管住嘴、迈开腿！")