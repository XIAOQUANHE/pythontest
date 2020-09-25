'''1、需要在前面添加前缀easygui'''
# import easygui
# easygui.msgbox('嗨，美女~')

'''2、直接调用，但是容易污染程序的命名空间'''
# from easygui import *
# msgbox('嘿，大美女~')

'''3、建议使用以下方法，保持EasyGui的命名空间，同时减少输入字符的数量：'''
# import easygui as eg
# eg.msgbox('嘿，超级美女~')
import easygui as eg
import sys

while 1:
    eg.msgbox("嗨，欢迎进入第一个界面小游戏^_^")      # 弹出对话框

    msg = "请问你希望在鱼C工作室学习到什么知识呢？"    # 对话框里面的提示
    title = "小游戏互动"                             # 对话框的title
    choices = ["谈恋爱","编程","游戏","琴棋书画"]     # 对话框里面的单选

    choice = eg.choicebox(msg,title,choices)

    # 注意，msgbox的参数是一个字符串
    # 如果用户选择Cancel,该函数返回None
    eg.msgbox("你的选择是：" + str(choice),"结果")

    msg = "你希望重新开始小游戏吗？"
    title = "请选择"

    # 弹出一个Continue/Cancel对话框
    if eg.ccbox(msg,title):
        pass        # 如果用户选择Continue
    else:
        sys.exit(0)  # 如果用户选择Cancel   退出编辑器