'''10.7 让用户输入密码'''
# 1 passwordbox()
import easygui as eg
# eg.passwordbox(msg='请输入密码：')

# 2 multpasswordbox()
# eg.multpasswordbox(msg='请输入用户名和密码：', title='登录', fields=("用户名：", "密码："))

'''10.8 显示文本'''
# 1 textbox()
file = open('..\\test_data\\record.txt')
eg.textbox(msg='文件【record.txt】的内容如下：',title='显示文本内容',text=file.read(),codebox=True)

# 2 codebox() 等宽字体显示文本内容（不自动换行）