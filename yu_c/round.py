'''列表末尾取出一个元素，将该元素插入到列表的最前边'''

list1 = [1,2,3,4,5,6,7,8]
num = len(list1)
for i in range(num):
    temp = list1.pop()
    list1.insert(0,temp)
    print(list1)
