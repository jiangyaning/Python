
def num(*a):
    # print(a)
    return len(a)
def max(*nums):
    n=sorted(nums,reverse=True)
    return n[0]
# a=input("请输入一组数,以空格分隔：").split()#将输入字符串转为列表
# b=tuple(int(x) for x in a)#将字符列表转为数字元组
# print("{0}的最大值为:{1},共{2}个数".format(b,max(b),num(b)))
print("(-1,34,-9,56)的最大值为:{0},共{1}个数".format(max(-1,34,-9,56),num(-1,34,-9,56)))
print("(1,4,6,95,3,78)的最大值为:{0},共{1}个数".format(max(1,4,6,95,3,78),num(1,4,6,95,3,78)))