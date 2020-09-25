# try:
#     f = open('我为什么是一个文档.txt')
#     print(f.read())
#     f.close()
# except OSError as reason:
#     print('文件打开过程中出错来T_T\n 错误原因是：' + str(reason))

# 1、针对不同异常设置多个except
# try:
#     sum = 1 + '1'
#     f = open('我是一个不存在的文档.txt')
#     print(f.read())
#     f.close()
# except OSError as reason:
#     print('文件出错啦T_T\n 错误原因是：' + str(reason))
# except TypeError as reason:
#     print('类型出错啦T_T\n 错误原因是：' + str(reason))

# 2、对多个异常统一处理
# try:
#     int('abc')
#     sum = 1 + '1'
#     f = open('我是一个不存在的文档.txt')
#     print(f.read())
#     f.close()
# except (OSError,TypeError) as reason:
#     print('出错啦T_T\n 错误原因是：' + str(reason))

# 3、捕获所有异常————————*不建议这样做*
try:
    int('abc')
    sum = 1 + '1'
    f = open('我是一个不存在的文档.txt')
    print(f.read())
    f.close()
except:
    print('出错啦~')

# *** 注意事项：try语句检测范围内一旦出现异常，剩下的语句将不会被执行。***