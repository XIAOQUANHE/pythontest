# 把数据存进文件，为了方便记忆，用.pkl或.pickle后缀名
import pickle   # 引入pickle模块
my_list = [123,3.14,'小甲鱼',['another list']]     # 列表，需要存入的数据
pickle_file = open(r'..\test_data\my_list.pkl','wb')    # 在指定的文件夹创建文件，以写入和二进制模式打开
pickle.dump(my_list,pickle_file)        # 使用dump方法存入指定路径里的文件中
pickle_file.close()                     # 关闭文件