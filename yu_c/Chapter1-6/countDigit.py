# 编写一个函数，分别统计出传入字符串参数（可能不止一个参数）的英文字母、空格、数字和其他字符的个数
def count(*param):
    length = len(param)     # 给的长度是2
    #print(length)
    for i in range(length):     #长度0：I love fishc.com    长度1：I love you, you love me.
        letters = 0     # 统计字母
        space = 0       # 统计空格
        digit = 0       # 统计数字
        others = 0      # 统计其他
        for each in param[i]:   # 遍历0里面的内容，i是0
            if each.isalpha():  # isalpha 统计字母
                letters += 1
            elif each.isdigit():    #isdigit 统计数字
                digit += 1
            elif each == ' ':       # 统计空格
                space += 1
            else:               # 统计其他
                others += 1
        print('第 %d 个字符串共有：英文字母 %d 个，数字 %d 个，空格 %d 个，其他字符 %d 个。'%(i+1,letters,digit,space,others))

count('I love fishc.com.','I love you, you love me.')