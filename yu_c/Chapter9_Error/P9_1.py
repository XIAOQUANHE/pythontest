# 1> AssertionError: 断言语句(assert)失败
# my_list = ["小甲鱼"]
# assert len(my_list) > 0
# print(my_list.pop())
#
# assert len(my_list) > 0

# 2> attributeError: 尝试访问未知的对象属性，当试图访问的对象属性不存在时抛出AttributeError异常：
# my_list = []
# my_list.fishc

# 3> IndexError: 索引超出序列的范围
# 在使用序列的时候就常常会遇到IndexError异常，原因是索引超出序列范围的内容：
# my_list = [1,2,3]
# my_list[3]          # 索引从0开始

# 4> KeyError：字典中查找一个不存在的关键字
# 当试图在字典中查找一个不存在的关键字就会引发KeyError异常，因此建议使用dict.get()方法:函数返回指定键的值，如果值不在字典中返回默认值。
# my_list = {"one":1,"two":2,"three":3}
# print(my_list["one"])
# my_list["four"]       # dict中没有key为‘four’

# 5> NameError: 尝试访问一个不存在的变量，当尝试访问一个不存在的变量时，Python会抛出NameError异常：
# fishc

# 6> OSError: 操作系统产生的异常，OSError，顾名思义就是操作系统产生的异常
# 像打开一个不存在的文件会引发FileNotFoundError，而这个fileNotFoundError就是OSError的子类。
# file_name = input('请输入要打开的文件名：')
# f = open(file_name,'r')
# print('文件的内容是：')
#
# for each_line in f:
#     print(each_line)

# 7> SyntaxError: Python的语法错误
# 如果遇到SyntaxError是Python的语法错误，这时Python的代码并不能继续执行，应该先找到并改正错误：
# print "I love fishc.com"        # 这是2.6版本的语法，不适用于3.x以上

# 8> TypeError: 不同类型间的无效操作，类型不同的对象是不能相互进行计算的，否则会抛出TypeError异常：
# 1 + "1"

# 9> ZeroDivisonError: 除数为零
# 地球人都知道除数不能为零，所以除以零就会引发ZeroDivisionError异常：
#5 / 0