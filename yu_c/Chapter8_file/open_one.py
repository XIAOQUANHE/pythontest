# 先在桌面创建一个record.txt的文本文件，内容随意
f = open(r"C:\Users\windows\Desktop\record.txt")
print(f.read())
print(f.tell())
print(f.seek(0,0))
print(f.read(5))
print(f.tell())
print(f.seek(0,0))
print(f.readline())
#f.write("这是一段待写入的数据")
f.close()

f = open(r"C:\Users\windows\Desktop\record.txt",'w')
f.write("这是一段待写入的数据")
f.close()

