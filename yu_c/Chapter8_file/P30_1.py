# 1. 编写一个程序，计算当前文件夹下所有文件的大小。
import os

os.chdir('..\\test_data\\os_size')      # 切换需要计算的文件夹
all_files = os.listdir(os.curdir)       # 使用os.curdir表示当前目录更标准
file_dict = dict()                      # 创建一个空的字典

for each_file in all_files:             # 遍历文件夹里面的文件
    if os.path.isfile(each_file):       # 判断指定路径是否存在且是一个文件
        file_size = os.path.getsize(each_file)  # getsize ——> 返回指定文件的尺寸，单位是字节，赋值给file_size变量
        file_dict[each_file] = file_size    # 字典的key是文件名，value是file_size


for each in file_dict.items():          # items：将字典类型转换为可遍历的元组
    print('%s【%dBytes】'% (each[0],each[1])) # 打印每次循环的key，value值，key是文件名，value值是字节