# 无参数版
# 1. 导包
import requests

# # 2.调用get
url = "http://www.baidu.com"
# r = requests.get(url)   # r: 为响应数据对象
#
# # 3.获取请求url地址
# print("请求url",r.url)
#
# # 4. 获取响应状态码
# print("状态码：", r.status_code)
#
# #5. 获取响应信息 文本形式
# print("文本响应内容：", r.text)

# 含参数版
'''
1.http://www.baidu.com?id=1001
2.http://www.baidu.com?id=1001,1002
3.http://www.baidu.com?id=1001&kw=北京
'''
# 参数：params
params = {"id":1001,"kw":"北京"}
r = requests.get(url,params=params)
# 3.获取请求url地址
print("请求url",r.url)

# 4. 获取响应状态码
print("状态码：", r.status_code)

#5. 获取响应信息 文本形式
print("文本响应内容：", r.text)