'''10.9 目录与文件'''
# 1、diropenbox() 目录名
import easygui as eg
# eg.diropenbox(msg='选择文件',title='文件系统')

# 2、fileopenbox() 文件名
# eg.fileopenbox(msg=None, title=None, default='D:\code\python\pythontest\yu_c\Chapter10_GUI\*.py',
# filetypes=["*.py"],multiple=False)

# 3、filesavebox()

'''10.10 捕获异常'''
# try:
#     print('I love FishC.com!')
#     int('FISHC') # 这里会产生异常
# except:
#     eg.exceptionbox()