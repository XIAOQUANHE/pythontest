# 2. 还记得求回文字符串那道题吗？现在让你使用递归的方式来求解，亲还能傲娇的说我可以吗？
"""
解题思路：有好多种方法，不过综合效率来说，小甲鱼的实现方法比较朴素，利用递归每次索引前后两个字符进行对比，当start > end的时候，
也正是首尾下标"碰面的时候，即作为递归结束的条件。"
"""
def is_palindrome(n, start, end):
    if start > end:             # 头标与尾标的索引进行对比
        return 1
    else:
        return is_palindrome(n,start+1,end-1) if n[start] == n[end] else 0   #头标与尾标的值进行对比

string = input('请输入一串字符串：')
length = len(string)-1      # 统计的是从1开始统计，值是从0开始获取下标，所以要 - 1
# print(len(string),length)

if is_palindrome(string, 0, length):
    print('"%s"是回文字符串！' % string)
else:
    print('"%s"不是回文字符串！' % string)
