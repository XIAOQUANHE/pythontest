'''1、self是什么'''
# class Ball:
#     def setName(self,name):
#         self.name = name
#     def kick(self):
#         print("我叫%s，奥~谁踢我？！" % self.name)
# a = Ball()
# a.setName("流光星陨")
# b = Ball()
# b.setName("月之光芒")
# c = Ball()
# c.setName("土豆")
# print(a.kick())
# print(b.kick())
# print(c.kick())

'''2、Python的魔法方法——> "__init__"'''
# class Potato:
#     def __init__(self,name):
#         self.name = name
#     def kick(self):
#         print("我叫%s，奥~谁踢我？！" % self.name)
# p = Potato("土豆")
# print(p.kick())

'''3、公有和私有'''
# 常用的点+属性名调用，无法调用！
# class Person:
#     __name = "小甲鱼"
#
# p = Person()
# p.__name

class Person:
    def __init__(self,name):
        self.__name = name
    def getName(self):
        return self.__name
p = Person("小甲鱼")
# p.__name
print(p.getName())
# 伪私有的原理 name mangling “_类名__变量名”
print(p._Person__name)