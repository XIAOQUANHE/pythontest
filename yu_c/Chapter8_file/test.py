f = open(r"../test_data/record.txt")
begin = 12

for i in range(begin):  # 用于消耗掉begin之前的内容
    print(f.readline())