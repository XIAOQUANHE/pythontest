'''10.4如何在buttonbox里面显示图片'''
import easygui as eg
# buttonbox 按钮
# choicebox 选择框
# multchoicebox 多选框
# eg.buttonbox('大家说我长得帅吗？',image='timg.gif', choices=('帅','不帅','!@#$%'))

'''10.5 为用户提供一系列选项'''
# eg.choicebox(msg='你最喜欢小甲鱼得哪些课程？', title='', choices=["《带你学C带你飞》","《零基础入门学习Python》",
# "《极客Python之效率革命》","《零基础入门学习Web开发》"])
#
# eg.multchoicebox(msg='你最喜欢小甲鱼得哪些课程？', title='', choices=["《带你学C带你飞》","《零基础入门学习Python》",
# "《极客Python之效率革命》","《零基础入门学习Web开发》"])