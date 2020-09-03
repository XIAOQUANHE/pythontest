#                                       ******7.1课间练习*****************
brand = ["李宁","耐克","阿迪达斯","鱼C工作室"]
slogan = ["一切皆有可能","Just do it","Impossible is nothing","让编程改变世界"]
print("鱼C工作室的口号是：%s" % slogan[brand.index("鱼C工作室")])
# 创建和访问字典
dict1 = {"李宁":"一切皆有可能","耐克":"Just do it","阿迪达斯":"Impossible is nothing","鱼C工作室":"让编程改变世界"}
print(dict1)
for each in dict1:
    print("%s -> %s" % (each,dict1[each]))

# 声明空字典
empty = {}
print(empty)
print(type(empty))

# 使用dict内置函数来创建字典
# 可以是一个序列(不能多个),打包成元组(列表)序列
dict2 = dict((('F',70),('i',105),('s',115),('h',104),('C',67)))
print(dict2)

# 映射关系参数创建字典
dict3 = dict(F=70, i=105, s=115, h=104, C=67)
print(dict3)

# 访问字典
# 相应的键放入方括号
print(dict3['C'])

# 字典键赋值，键存在，改写对应值；键不存在，创建新键并赋值
dict3['x'] = 88
print(dict3)
dict3['x'] = 120
print(dict3)

# 字典键唯一性，如后面出现相同键，后一个值会被记住
courses = {"小甲鱼":"《零基础入门学习Python》","不二如是":"《零基础入门学习Scratch》","小甲鱼":"《极客Python之效率革命》"}
print(courses)

# 键不可变，可用数值、字符串、元组，不可用列表
dict1 = {(1,2,3):"One Two Three", 1:"One", 2:"Two", 3:"Three"}
print(dict1)

# dict1 = {[1,2,3]:"One Two Three", 1:"One", 2:"Two", 3:"Three"}
# print(dict1)

# 列举五种方法创建同样的字典
a = dict(one=1, two=2, three=3)
b = {'one': 1,'two': 2,'three': 3}
c = dict(zip(['one','two','three'],[1,2,3]))
d = dict([('two',2), ('one',1), ('three',3)])
e = dict({'three':3, 'one':1, 'two':2})
print(a == b == c == d == e)
print(a,'\n',b,'\n',c,'\n',d,'\n',e)

# 字典不支持拼接和重复操作
# f = d + e
# print(f)

# g = 3 * a
# print(g)