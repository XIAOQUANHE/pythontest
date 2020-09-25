'''1.要么怎样，要么不怎样
if 条件：
    条件为真执行
else:
    条件为假执行
'''

'''2.干完了能怎样，干不完就别想怎样'''
# def showMaxFactor(num):
#     count = num // 2
#     while count > 1:
#         if num % count == 0:
#             print('%d最大的约数是%d' %(num,count))
#             break
#         count -= 1
#     else:
#         print('%d是素数！' % num)
# num = int(input('请输入一个数：'))
# showMaxFactor(num)

# '''3.没有问题？那就干吧'''
# try:
#     print(int('abc'))
# except ValueError as reason:
#     print('出错啦：' + str(reason))
# else:
#     print('没有任何异常！')

'''————————————————9.6、简洁的with语句————————————————'''
# try:
#     with open('data.txt','w') as f:
#         for each_line in f:
#             print(each_line)
# except OSError as reason:
#     print('出错啦：' + str(reason))
