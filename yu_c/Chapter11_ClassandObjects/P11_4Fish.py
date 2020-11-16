'''金鱼(Goldfish)、鲤鱼(Carp)、鲨鱼(Shark)，还有三文鱼(Salmon)'''
import random as r

class Fish:
    def __init__(self):
        self.x = r.randint(0,10)
        self.y = r.randint(0,10)

    def move(self):
        # 这里主要演示类的继承机制，就不考虑检查场景边界和移动方向的问题
        # 假设所有鱼都是一路向西游
        self.x -= 1
        print("我的位置是：",self.x,self.y)

class Goldfish(Fish):
    pass

class Carp(Fish):
    pass

class Salmon(Fish):
    pass

# 上面几个都是食物，食物不需要有个性，所以直接继承Fish类的全部属性和方法即可
# 下面定义鲨鱼类，这个是吃货，除了继承Fish类的属性和方法，还有添加一个吃的方法

class Shark(Fish):
    def __init__(self):
        super().__init__()      # super()函数，自动找出所有基类以及对应方法。
        self.hungry = True

    def eat(self):
        if self.hungry:
            print("吃货的梦想就是天天有得吃^_^")
            self.hungry = False
        else:
            print("太撑了，吃不下！")

fish = Fish()
print(fish.move())

goldfish = Goldfish()
print(goldfish.move())
print(goldfish.move())
print(goldfish.move())

shark = Shark()
print(shark.eat())
print(shark.eat())
print(shark.move())
