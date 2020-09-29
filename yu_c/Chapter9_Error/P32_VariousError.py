'''1. 请问以下代码是否会产生异常，如果会的话，请写出异常的名称：'''
# my_list = [1,2,3,4,,]     # SyntaxError:语法错误 invalid syntax

'''2. 请问以下代码是否会产生异常，如果会的话，请写出异常的名称：'''
# my_list = [1,2,3,4,5]
# print(my_list[len(my_list)])      #IndexError: 索引错误 list index out of range

'''3. 请问以下代码是否会产生异常，如果会的话，请写出异常的名称：'''
# my_list = [3,5,1,4,2]
# my_list.sorted()          # AttributeError: 尝试访问未知的对象属性 'list' object has no attribute 'sorted'

'''4. 请问以下代码是否会产生异常，如果会的话，请写出异常的名称：'''
# my_dict = {'host':'http://bbs.fishc.com','port':'80'}
# print(my_dict['server'])            # KeyError: 键异常，该字典中没有该key ‘server’，使用dict.get()方法避免

# if not my_dict.get('server'):                 # if not 为假时执行语句
#     print('您所访问的键【server】不存在！')     # 判断该key是否存在，不存在——打印提示信息

'''5. 请问以下代码是否会产生异常，如果会的话，请写出异常的名称：'''
# def my_fun(x,y):    # SyntaxError：语法错误 positional argument follows keyword argument
#     print(x,y)

# my_fun(x=1,2)       # 如果使用关键字参数的话，需要两个参数均使用关键字参数my_fun(x=1,y=2)

'''6. 请问以下代码是否会产生异常，如果会的话，请写出异常的名称：'''
# f = open('C:\\test.txt',wb)         # NameError: 变量错误 open()第二个参数是字符串，不加引号以为是变量
# f.write('I love fishC.com!\n')      # 会报 name 'wb' is not defined 未定义
# f.close()

'''7. 请问以下代码是否会产生异常，如果会的话，请写出异常的名称：'''
# def my_fun1():
#     x = 5
#     def my_fun2():
#         x* = x              # SyntaxError: 语法错误 invalid syntax 局部变量x找不到
#         return x
#     return my_fun2()
#
# my_fun1()

'''代码改造：
在python3z之前没有直接的解决方案，只能间接地通过容器类型来存放，因为容器类型不是放在栈里，所以不会被“屏蔽掉”。
容器类型这个词就是字符串、列表、元组，这些都是容器类型。
'''
# def my_fun1():
#     x = [5]
#     def my_fun2():
#         x[0] *= x[0]
#         return x[0]
#
# my_fun1()

'''但是到了Python3的世界里，又有了不少的改进，如果我们希望在内部函数里可以修改外部函数里的局部变量的值，
那么也有一个关键字可以使用，就是nonlocal：
'''
# def my_fun1():
#     x = 5
#     def my_fun2():
#         nonlocal x
#         x *= x
#         return x
#     return my_fun2()
#
# f = my_fun1()
# print(f)
