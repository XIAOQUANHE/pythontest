# 0. 编写一个程序，统计当前目录下每个文件类型的文件数
import os
os.chdir("..\\test_data\\os")       # os.chdir ——> 切换到目标目录下
all_files = os.listdir(os.curdir)   #使用os.curdir表示当前目录更标准
type_dict = dict()  # 创建一个空字典
print(all_files)
for each_file in all_files:     # 遍历取目录里面的文件
    if os.path.isdir(each_file):    # isdir ——> 判断指定路径是否存在且是一个目录
        # 如果该目录下还有目录，执行该条if语句
        type_dict.setdefault('文件夹',0)   # setdifault(keyname, value) ——> keyname存在，取value值，不存在，新建key，赋值value
        type_dict['文件夹'] += 1           # 相同的keyname，value值+1
    else:
        ext = os.path.splitext(each_file)[1]  # splitext——> 分离文件名与扩展名，返回(f_name,f_extension)元组
        # 返回格式('test', '.py')，是一个元组(tuple),需要取扩展名，需要加上下标[1]
        type_dict.setdefault(ext, 0)  # setdifault(keyname, value) ——> keyname存在，取value值，不存在，新建key，赋值value
        type_dict[ext] += 1           # 相同的keyname，value值+1

for each_file in type_dict.keys():   # 字典里面的keys是唯一的，遍历keys，取keys的value
    print('该文件下共有类型为【%s】的文件 %d 个' %(each_file,type_dict[each_file]))