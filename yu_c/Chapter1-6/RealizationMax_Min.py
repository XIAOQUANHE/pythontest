#min()的这个BIF实现过程
nums = [1,23,4,57,63,6]
min = nums[0]
for each in nums:
    if each < min:
        min = each
print(min)

# max()的这个BIF实现过程
max = nums[0]
for each in nums:
    if each > max:
        max = each
print(max)

# 函数定义min方法实现过程
def min(x):
    least = x[0]
    for each in x:
        if each < least:
            least = each
    return least
print(min('123456789'))