'''1、默认参数和关键字参数'''
# 默认参数
import easygui as eg
# eg.msgbox('我爱小甲鱼^_^')
# eg.msgbox('我爱小甲鱼^_^', '鱼油心声')

# 关键字参数
choices = ['愿意','不愿意','有钱的时候就愿意']
reply = eg.choicebox('你愿意购买资源打包支持小甲鱼吗？',choices=choices)

'''10_3
1、使用按钮组件'''
import easygui as eg
# 1.1 msgbox()
'''msgbox(msg='(Your message goes here)', title=' ', ok_button='OK',image=None,root=None)
msgbox()函数显示一个消息和提供一个OK按钮，可以指定任意的消息和标题，甚至可以重写OK按钮的内容：'''
# eg.msgbox('我一定要学回编程！',ok_button='加油！')

# 1.2 ccbox()
'''ccbox(msg='Shall    I    continue?', title=' ', choices=('C[o]ntinue','C[a]ncel'), image=None, 
default_choice='C[o]ntinue', cancel_choice='C[a]ncel')
ccbox()函数提供一个选择：C[o]ntinue或者C[a]ncel,并相应返回True或者False。[o]&[a]：快捷键'''

# 1.3 ynbox()
'''ynbox(msg='Shall I continue?',title='',choices=('[<F1>]YES','[<F2>]No'),
image=None, default_choice='[<F1>]YES', cancel_choice='[<F2>]No')'''

# 1.4 buttonbox()
'''buttonbox(msg='',title='',choices=('Button[1]','Button[2]','Button[3]'),image=None, images=None,
default_choice=None,cancel_choice=None,callback=None,run=True)'''
# title = '你喜欢以下哪一种水果？'
# eg.buttonbox(title,choices=('草莓','西瓜','芒果'))

# 1.5 indexbox()
'''indexbox(msg = 'Shall  I  continue?', title=' ', choices=('Yes', 'No'),
image=None, default_choice='Yes', cancel_choice='No')'''

# 1.6 boolbox()
'''boolbox(msg='Shall I continue?', title=' ', choices=('(Y)es', '[N]o'),
image=None, default_choice='Yes', Cancel_choice='No')'''