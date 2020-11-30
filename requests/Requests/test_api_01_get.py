# 导包
import requests as rs
# 淘宝的查询手机号码归属地接口
'''
接口的URL地址 "http://tcc.taobao.com/cc/json/mobile_tel_segment.htm"
接口的请求参数：tel
接口的请求方式：get
'''

# 定义一个变量
# url = "http://tcc.taobao.com/cc/json/mobile_tel_segment.htm"
# get请求，请求的数据有两种方式
# 1 请求参数保存在url里面,?后面添加参数名与参数值，如果有多个参数，用&连接
# url = "http://tcc.taobao.com/cc/json/mobile_tel_segment.htm?tel=17688829122"
# r = rs.get(url=url)
# print(r.text)
# print(r.status_code)
# print(r.cookies)
# print(r.url)
# 2 参数保存在 params   参数用字典格式进行保存
url = "http://tcc.taobao.com/cc/json/mobile_tel_segment.htm"
params = {
    "tel":17688829122
}
r = rs.get(url=url,params=params)
print(r.text)
print(r.status_code)
print(r.cookies)
print(r.url)