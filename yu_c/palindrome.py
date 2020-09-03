'''
编写一个函数，判断传入的字符串参数是否为“回文联”（回文联即用回文形式写成的对联，即可顺读，也可倒读，例如：上海自来水来自海上）
'''
# 方法一
'''
def palindrome(string):
    length = len(string)    # 3、获取用户输入字符的长度
    last = length-1         # 4、获取的长度减1，如有123，获取长度为3，但是编程的索引从0开始，实际值0，1，2
    length //=2             # 5、长度地板除2，分成两半
    flag = 1                # 6、后面对比判断字段
    for each in range(length):  # 遍历length的长度
        if string[each] != string[last]:    # 前半字符与后半字符对比
            flag = 0                        # 如果不相等，赋值flag=0
        last -= 1           # last变量减 1
    if flag == 1:
        return 1
    else:
        return 0

string = input('请输入一句话：')   # 1、获取用户输入文字
if palindrome(string) == 1:     # 2、调用函数，获取return做比较
    print('是回文联！')
else:
    print('不是回文联！')
'''
# 方法二
def Palindrome(string):
    list1 = list(string)
    list2 = reversed(list1)
    if list1 == list(list2):
        return '是回文联'
    else:
        return '不是回文联！'
print(Palindrome('上海自来水来自海上'))