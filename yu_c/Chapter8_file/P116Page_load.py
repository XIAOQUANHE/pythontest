# 使用.load()方法加载数据，与P115Page_pickle.py相呼应
import pickle

pickle_file = open(r'..\test_data\my_list.pkl','rb')        # 以只读和二进制模式打开文件
my_list = pickle.load(pickle_file)                          # 使用.load加载数据
print(my_list)                                              # 打印加载出来的数据