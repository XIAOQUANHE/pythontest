# requests 发送post请求，主要是讲2钟请求数据格式
# 一种数据格式 from-data 表单格式
# 二种数据格式，json
# 案例
'''
1,注册接口，数据格式是data格式
url地址：http://106.12.126.197:8000/register
请求方式：post请求
请求参数：username password
2, 登录接口，数据格式是json格式
url地址：http://106.12.126.197:8000/login
请求方式：post请求
请求参数：username password
'''
# 导包
import requests as rs
# 1,注册接口
url_reg = "http://106.12.126.197:8000/register" # 假接口
# 表单数据格式，参数data，数据都是字典去保存
data = {
    "username":"hxq1001",
    "password":"hxq123456"
}
# 发送请求 表单格式的数据，用data
r_reg = rs.post(url=url_reg,data=data)
print(r_reg.text)
print(r_reg.status_code)
print(r_reg.cookies)
print(r_reg.url)

# 2,登录接口，数据格式 json格式
url_login = "http://106.12.126.197:8000/login"  # 假接口
# json格式数据，定义值，也是用字典格式保存，json
json = {
    "username":"hxq1001",
    "password":"isadfjsadlkfjaskfdajoifajfalkjaoidsjf0329uklj"
}
# 发送请求，请求参数 json
r_login = rs.post(url=url_login,json=json)
print(r_reg.text)
print(r_reg.status_code)
print(r_reg.cookies)
print(r_reg.url)