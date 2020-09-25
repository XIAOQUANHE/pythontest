'''9.2、try-finally 语句
文件打开了，关闭文件的命令被跳过了
'''
# try:
#     f = open('我是一个不存在的文档.txt')
#     print(f.read())
#     sum = 1 + '1'
#     f.close()
# except:
#     print('出错啦')

'''9.3、finally,就算出现异常，但也不得不执行的收尾工作(如在程序崩溃前保存用户文档)
try语句块中没有出现任何运行时错误，会跳过except语句块执行finally语句块的内容，
出现异常，先执行except语句块的内容再执行finally语句块的内容，finally语句块一定会被执行！
'''
# try:
#     f = open('我是一个不存在的文档.txt','w')
#     print(f.write('我存在了！\n'))
#     sum = 1 + '1'
#     f.close()
# except:
#     print('出错了')
# finally:
#     print(f.write('第二次存在了！'))           # 当执行了except语句了，文件依然是打开状态
#     f.close()

'''9.4、 raise 语句：抛出一个异常，抛出的异常还可以带参数，表示异常的解释'''
# raise ZeroDivisionError
# raise ZeroDivisionError("除数不能为零！")