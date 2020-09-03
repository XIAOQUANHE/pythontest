#                                  ******7.1.2课间练习-内置方法*****************
# 1、fromkeys(seq[,value]) 创建字典，键[,值]
# dict1 = {}
# print(dict1.fromkeys((1,2,3)))
#
# dict2 = {}
# print(dict2.fromkeys((1,2,3),"Number"))
#
# dict3 = {}
# print(dict3.fromkeys((1,2,3),("one","two","three")))

# 2、keys(), values(), items()，返回键，值，键值对
dict1 = {}
dict1 = dict1.fromkeys(range(32),"赞")
print(dict1.keys())     # 用于返回字典中的键
print(dict1.values())   # 用于返回字典中所有的值
print(dict1.items())    # 返回字典中所有的键值对

# print(dict1[32])        # 不存在的项，python报错

# 3、get(key[,default]) 键不存在，返回None，或设置default值返回
print(dict1.get(31))
print(dict1.get(32))
print(dict1.get(32,"没有该值"))
print(31 in dict1)
print(32 in dict1)

# 4、清空一个字典，clear()方法
print(dict1)
dict1.clear()
print(dict1)

# 赋值空字典清空字典弊端
a = {"姓名":"小甲鱼", "密码":"123456"}
b = a
print(b)
a = {}
print(a)
print(b)

# 只是a指向了一个空字典，b未改变，容易被窃取，用clear()方法
a = {"姓名":"小甲鱼", "密码":"123456"}
b = a
print(b)
a.clear()
print(a)
print(b)

# 5、copy()方法用于拷贝(浅拷贝)整个字典
a = {1:"one", 2:"two", 3:"three"}
b = a.copy()
print(id(a))    # 内存id不一样
print(id(b))
a[1] = "four"   # 修改了a，b的键值对并没有改变
print(a)
print(b)

# 6、pop(key[,default]) 和 popitem()
# pop()是给定键弹出对应的值，而popitem()是弹出一个项
a = {1:"one", 2:"two", 3:"three", 4:"four"}
print(a.pop(2))
print(a)

print(a.popitem())
print(a)

# 7、setdefault(key[,default]),setdefault()在字典中找不到相应的键时会自动添加
a = {1:"one", 2:"two", 3:"three", 4:"four"}
print(a.setdefault(3))
print(a.setdefault(5))
print(a)

# 8、update([other]),更新字典
pets = {"米奇":"老鼠", "汤姆":"猫", "小白":"猪"}
pets.update(小白="狗")
print(pets)

test = {1:"one"}
test[2] = "two"
print(test)