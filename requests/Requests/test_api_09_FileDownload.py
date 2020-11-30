# requests里面的一个stream 文件下载的一个参数
# 举例说明： CORNERSTONE 导出测试计划
import requests as rs
url = 'https://cs.cornerstone365.cn/p/file/download_file/336a3ed2f6654610a2b7916cee4257ae.xlsx?token=af8dc5c91239496f96307bd747071cce'

cookies = {
        'Cookie': 'SERVER_ID=CornerstoneWebSystemPrd; token=af8dc5c91239496f96307bd747071cce'
        }

r = rs.get(url=url,cookies=cookies)
r.encoding = 'gb312'
print(r.status_code)
print(r.encoding)
print(r.text)
# 逻辑，需要把返回的请求信息，返回字符串，把这些字符串信息，写入到，对应文件里面
# 乱码问题没有解决，先暂停解决
# 写入文件
with open(r'../image/test.xlsx','wb') as f:     # 打开文件进行写入操作，with目的，如果文件不存在，也不会报错
    # 判断返回成功，把返回的信息，写入到 test.xlsx文件里面
    if r.status_code == 200:        # 状态码为200时候，写入文件
        for chunk in r.iter_content(chunk_size=1): # inter_content 循环去读取信息写入，chunk_size=1 文件大小
            f.write(chunk) # 把循环读取的值，写入test.xlsx文件里面
    # 写入文件成功，文件内容是不是乱码，只是返回的字符串是乱码

'''总结下思路：
1、发送接口请求
2、把写入到下载文件中，去保存
3、stream false(大文件)，true(内存不够，把参数修改成true)，默认为false
如果大家工作当中遇到文件下载接口，如何去校验下载的文件是否正确
1、期望值
2、读取文件里面的值，去对比，需要调用python打开文件内容
'''
