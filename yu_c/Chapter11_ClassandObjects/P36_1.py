'''1. 按照以下提示尝试定义一个矩形类并生成类实例对象。
    属性：长和宽
    方法：设置长和宽 -> setRect(self)，获得长和宽 -> getRect(self)，获得面积 -> getArea(self)
    提示：方法中对属性的引用形式需加上 self，如 self.width'''
class Rectangle:
    longth = 5
    width = 4

    def setRect(self):  # 设置长和宽
        print("请输入矩形的长和宽...")
        self.longth = float(input("长："))
        self.width = float(input("宽："))

    def getRect(self):  # 获取长和宽
        print("这个矩形的长是：%.2f，宽是：%.2f" %(self.longth,self.width))

    def getArea(self):  # 获得面积
        print (self.longth*self.width)

rect = Rectangle()
rect.getRect()
rect.setRect()
rect.getRect()
rect.getArea()
