'''0. 按照以下要求定义一个游乐园门票的类，并尝试计算2个成人+1个小孩平日票价。
    平日票价100元
    周末票价为平日的120%
    儿童半票'''
class Ticket:   # 定义一个门票类
    def __init__(self,weekend = False, child = False):  # 构造方法，默认值为：不是周末，没有小孩
        self.exp = 100      # 平日票价为100
        if weekend:         # 判断是否为周末
            self.inc = 1.2  # 是周末，为120%
        else:
            self.inc = 1    # 不是周末，为100%
        if child:           # 判断你是否有小孩
            self.min = 0.5  # 有小孩，半价
        else:
            self.min = 1    # 没有小孩，原价
    def calcPrice(self,num):    # 定义一个方法，实例化的时候可以传入人数
        return self.exp * self.inc * self.min * num     # 计算门票
p = Ticket()            # 实例化对象为p
b = Ticket(child=True)  # 实例化堆笑为b，传入有小孩
# 调用方法，p为默认配置，有两个人，b有小孩1个
print("2个成人和一个小孩平日票价为: %.2f" %(p.calcPrice(2) + b.calcPrice(1)))