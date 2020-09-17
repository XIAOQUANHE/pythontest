# 编写一个进制转换程序，程序演示如下（提示，十进制转换二进制可以用bin()这个BIF）
q = True
while q:
    num = input("请输入一个整数(输入Q结束程序)：")
    if num != 'Q':
        num = int(num)
        print('十进制 -> 十六进制： %d -> %#x' %(num,num))  # %#x:在八进制数前面显示零（'0'）,在十六进制数前面显示'0x'或'0X'
        print('十进制 -> 八进制： %d -> %#o' %(num,num))
        print('十进制 -> 二进制：%d -> '% num,bin(num))    #bin()返回一个整数int或者长整数long int 的二进制表示
    else:
        q = False