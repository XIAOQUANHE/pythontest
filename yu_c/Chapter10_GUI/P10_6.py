'''10.6 让用户输入消息'''
import easygui as eg
# 1 enterbox() 输入框，返回值为用户输入字符串
# eg.enterbox(msg='请输入一句你最想对小甲鱼说的话：')

# 2 integerbox() 范围内lowerbound最小值，upperbound最大值的整数数值
# P10_2.py
# import random
# import easygui as eg
#
# eg.msgbox("嗨，欢迎进入第一个界面小游戏^_^")
# secret = random.randint(1,10)
#
# msg = "不妨猜一下小甲鱼现在心里想的是哪个数字(1~10):"
# title = "数字小游戏"
# guess = eg.integerbox(msg,title,lowerbound=1,upperbound=10)
#
# while True:
#     if guess == secret:
#         eg.msgbox("卧槽，你是小甲鱼心里的蛔虫吗？！")
#         eg.msgbox("哼，猜中了也没有奖励！")
#         break
#     else:
#         if guess > secret:
#             eg.msgbox("哥，大了大了~~~")
#         else:
#             eg.msgbox("嘿，小了小了~~~")
#         guess = eg.integerbox(msg,title,lowerbound=1,upperbound=10)
# eg.msgbox("Game over！ see you")

# 3 multenterbox() 提供多个输入框
import easygui as eg

msg = "请填写以下联系方式"
title = "账号中心"
fieldNames = [" *用户名", " *真实姓名", " 固定电话", " *手机号码", " QQ", " *E-mail"]
fieldValues = []
fieldValues = eg.multenterbox(msg,title,fieldNames)

while 1:
    if fieldValues == None:
        break
    errmsg = ""
    for i in range(len(fieldNames)):
        option = fieldNames[i].strip()
        if fieldValues[i].strip() == "" and option[0] == "*":
            errmsg += ('【%s】为必填项。\n\n' % fieldNames[i])
    if errmsg == "":
        break
    fleldValues = eg.multenterbox(errmsg,title,fieldNames,fieldValues)
print("用户资料如下：%s" % str(fieldValues))
