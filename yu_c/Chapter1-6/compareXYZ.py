print("--------------三个整数比较大小---------------")

x,y,z = 6,5,4
small = (x if x < y else y)
small = (z if small > z else small)
print(small)
