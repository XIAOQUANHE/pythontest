# 动动手
# 0 尝试将文件（  OpenMe.mp3 (700 Bytes, 下载次数: 15716) ）打印到屏幕上
f=open(r"D:\code\python\pythontest\yu_c\test_data\OpenMe.mp3")
for each_line in f:
    print(each_line,end='')

# 1. 编写代码，将上一题中的文件（OpenMe.mp3）保存为新文件（OpenMe.txt）
f1 = open(r"D:\code\python\pythontest\yu_c\test_data\OpenMe.mp3")
f2 = open(r"D:\code\python\pythontest\yu_c\test_data\OpenMe.txt",'x')
f2.write(f1.read())     #write(str)：将字符串str写入文件
f2.close()
f1.close()