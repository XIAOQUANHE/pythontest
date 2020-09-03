#               ******7.2集合：在我的世界里，你就是唯一*****************
# 1、大括号没有体现映射关系，是集合。
num1 = {}
print(type(num1))   # <class 'dict'>
num2 = {1,2,3,4,5}
print(type(num2))   # <class 'set'>

# 2、唯一性，自动去重复数据
num = {1,2,3,4,5,5,4,3,2,1}
print(num)  # {1, 2, 3, 4, 5}

# 3、集合是无序，不能索引元素
# print(num[2])   # TypeError: 'set' object does not support indexing “set” 对象不支持索引

#               ****** 7.2.1 创建集合*****************
# 1、两种，用大括号{}，用set()内置函数
set1 = {"小甲鱼","小鱿鱼","小鲤鱼","小甲鱼"}
set2 = set({"小甲鱼","小鱿鱼","小鲤鱼","小甲鱼"})
print(set1 == set2)      # True