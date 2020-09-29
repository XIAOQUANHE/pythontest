'''测试题 5、请恢复以下代码中马赛克挡住的内容，使得程序执行后可以按要求输出。
try:
    for i in range(3):
        for j in range(3):
            ***
            ***
            print(i,j)
except KeyboardInterrupt:
    print('退出啦！')

输出：
0 0
0 1
0 2
1 0
1 1
1 2
退出啦！
'''
# try:
#     for i in range(3):
#         for j in range(3):
#             if i == 2:
#                 raise KeyboardInterrupt
#             print(i,j)
# except KeyboardInterrupt:
#     print('退出啦！')

'''动动手：
0. 还记得我们第一个小游戏吗？只要用户输入非整型数据，程序立刻就会蹦出不和谐的异常信息然后崩溃。
请使用刚学的异常处理方法修改以下程序，提高用户体验。
猜数字小游戏：'''
import random

secret = random.randint(1,10)
print('------------------我爱鱼C工作室------------------')
temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字：")
try:
    guess = int(temp)
except ValueError:
    print("只支持整数哦！")
    guess = secret
while guess != secret:
    temp = input("哎呀，猜错了，请重新输入吧：")
    guess = int(temp)
    if guess == secret:
        print("我草，你是小甲鱼心里的蛔虫吗？！")
        print("哼，猜中了也没有奖励！")
    else:
        if guess > secret:
            print("哥，大了大了~~~")
        else:
            print("嘿，小了，小了~~~")
print("游戏结束，不玩啦^_^")
