'''1. 游戏编程：按以下要求定义一个乌龟类和鱼类并尝试编写游戏。
（初学者不一定可以完整实现，但请务必先自己动手，你会从中学习到很多知识的^_^）
    假设游戏场景为范围（x, y）为0<=x<=10，0<=y<=10
    游戏生成1只乌龟和10条鱼
    它们的移动方向均随机
    乌龟的最大移动能力是2（Ta可以随机选择1还是2移动），鱼儿的最大移动能力是1
    当移动到场景边缘，自动向反方向移动
    乌龟初始化体力为100（上限）
    乌龟每移动一次，体力消耗1
    当乌龟和鱼坐标重叠，乌龟吃掉鱼，乌龟体力增加20
    鱼暂不计算体力
    当乌龟体力值为0（挂掉）或者鱼儿的数量为0游戏结束
'''
import random as r

legal_x = [0,10]
legal_y = [0,10]

# print(legal_x[0])     # 按照下标取值 0
# print(legal_x[1])     # 按照下标取值 10
class Turtle:
    def __init__(self):
        # 初始体力
        self.power = 100
        # 初始位置随机
        self.x = r.randint(legal_x[0],legal_x[1])   # 下标0为0，下标1为10
        self.y = r.randint(legal_y[0],legal_y[1])   # 下标0为0，下标1为10

    def move(self):
        # 随机计算方向并移动到新的位置(x,y)
        new_x = self.x+r.choice([1,2,-1,-2])        # x随机位置加上choice随机获取到的数据，变成新的位置信息
        new_y = self.y+r.choice([1,2,-1,-2])        # y随机位置加上choice随机获取到的数据，变成新的位置信息
        print(new_x,new_y)
        # 检查移动后是否超出场景x轴边界
        if new_x < legal_x[0]:
            self.x = legal_x[0] - (new_x - legal_x[0])  # x移动的位置小于0，自动向反反向移动n点
        elif new_x > legal_x[1]:
            self.x = legal_x[1] - (new_x - legal_x[1])  # x移动的位置大于10，自动向反反向移动n点
        else:
            self.x = new_x
        # 检查移动后是否超出场景y轴边界
        if new_y < legal_y[0]:
            self.y = legal_y[0] - (new_y - legal_y[0])  # y移动的位置小于0，自动向反反向移动n点
        elif new_y > legal_y[1]:
            self.y = legal_y[1] - (new_y - legal_y[1])  # y移动的位置小于0，自动向反反向移动n点
        else:
            self.y = new_y
        # 体力消耗
        self.power -= 1
        # 返回移动后的新位置
        return(self.x,self.y)
    def eat(self):
        self.power += 20
        if self.power > 100:
            self.power = 100    # 上线体力为100，吃鱼只有如果大于100，调整为100
class Fish:
    def __init__(self):
        self.x = r.randint(legal_x[0],legal_x[1])
        self.y = r.randint(legal_y[0],legal_y[1])

    def move(self):
        # 随机计算方向并移动到新的位置(x,y)
        new_x = self.x + r.choice([1,-1])
        new_y = self.y + r.choice([1,-1])
        # 检查移动后是否超出x轴边界
        if new_x < legal_x[0]:
            self.x = legal_x[0] - (new_x - legal_x[0])
        elif new_x > legal_x[1]:
            self.x = legal_x[1] - (new_x - legal_x[1])
        else:
            self.x = new_x
        # 检查移动后是否超出y轴边界
        if new_y < legal_y[0]:
            self.y = legal_y[0] - (new_y - legal_y[0])
        elif new_y > legal_y[1]:
            self.y = legal_y[1] - (new_y - legal_y[1])
        else:
            self.y = new_y
        # 返回移动后的位置
        return(self.x,self.y)

turtle = Turtle()
fish = []       # ()tuple，[]list，{}dict
for i in range(10):
    new_fish = Fish()       # 实例化一个对象
    fish.append(new_fish)   # 获取10条鱼的初始位置添加到fish列表里面

while True:             # 判断鱼的数量和乌龟的体力
    if not len(fish):   # 判断鱼的数量
        print("鱼儿都吃完了，游戏结束！")
        break
    if not turtle.power:    # 判断乌龟的体力
        print("乌龟体力耗尽，挂掉了！")
        break

    pos = turtle.move()     # 把返回来的x轴和y轴赋值给pos，例如：3，4
    # 在迭代器中删除列表元素是非常危险的，经常会出现意想不到的问题，因为迭代器是直接引用列表的数据进行引用
    # 这里我们把列表拷贝给迭代器，然后对原列表进行删除操作就不会有问题了^_^
    for each_fish in fish[:]:   # 遍历fish的初始位置
        if each_fish.move() == pos: # 1-10条鱼移动后的位置，每一条都和乌龟的位置对比
            # 鱼儿被吃掉了
            turtle.eat()            # 有鱼的位置和乌龟位置相同，调用吃的方法，增加体力
            fish.remove(each_fish)  # 删除fish列表中的一条鱼
            print("有一条鱼儿被吃掉了...")

