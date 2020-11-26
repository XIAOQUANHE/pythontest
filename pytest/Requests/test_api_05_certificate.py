# 举例说明，携程网
import requests as rs
url = 'https://www.ctrip.com'
# 解决方案1
# 发送请求时候忽略证书，证书的参数verify-用的比较多
r = rs.get(url=url,verify=False)        # verify参数默认为True，值为FALSE 表示忽略证书
print(r.text)

# 解决方案2，verify里面添加证书的路径
r = rs.get(url=url,verify='路径')        # verify参数默认为True，值为FALSE 表示忽略证书
print(r.text)