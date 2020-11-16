'''11.4  继承
类继承的语法：
class 类名(被继承的类):
    ...
'''
# class Parent:
#     def hello(self):
#         print("正在调用父类的方法...")
# class Child(Parent):
#     pass
#
# p = Parent()
# print(p.hello())
#
# c = Child()
# print(c.hello())

'''子类中定义与父类同名的方法或属性，则会自动覆盖父类对应的方法或属性，父类不受影响'''
# class Child(Parent):
#     def hello(self):
#         print("正在调用子类的方法...")
# c = Child()
# print(c.hello())
# print(p.hello())

'''多重继承'''
class Base1:
    def fool(self):
        print("我是fool，我在Base1中...")

class Base2:
    def foo2(self):
        print("我是foo2，我在Base2中...")

class C(Base1,Base2):
    pass

c = C()
print(c.fool())
print(c.foo2())