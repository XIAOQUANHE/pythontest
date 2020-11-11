'''0、先练练手，把我们的刚开始的那个猜数字小游戏加上界面吧？'''
import random
import easygui as eg

eg.msgbox("嗨，欢迎进入第一个界面小游戏^_^")
result = random.randint(1,10)   # 随机获得此区间的一位整数

title = '数字小游戏'
msg = '不妨猜一下小甲鱼现在心里想的是哪个数字(1-10)：'
receive = eg.integerbox(msg,title,lowerbound=1,upperbound=10)   # 接收用户输入的整型数值

while True:
    if result == receive:
        eg.msgbox(msg='猜对了，恭喜你！')
        eg.msgbox(msg='(￢︿̫̿￢☆)')
        break
    else:
        if result > receive:
            eg.msgbox(msg='小了小了！')
        else:
            eg.msgbox(msg='大了大了！')
        receive = eg.integerbox(msg, title, lowerbound=1, upperbound=10)  # 接收用户输入的整型数值
eg.msgbox("game over！")