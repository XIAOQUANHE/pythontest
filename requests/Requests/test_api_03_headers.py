# requests的headers请求参数
# 举例说明
# headers发送请求，这个参数不是每个接口都必须要添加，都是开发定义
'''
两个例子
前程无忧搜索职位接口
一个是12306查询车票的接口，需要添加参数headers
'''
# 第一个前程无忧，查询职位接口
# 需要测试接口，需要请求url地址，参数，请求方式，目前通过抓包获取
'''
步骤：
1、打开前程无忧的网站
2、打开前程无忧的调试工具（一般默认快捷键是F12）
3、打开调试工具-选择network，进行抓包，如果原来里面有抓包信息，大家先清空下，点击clear
4、搜索职位，点击查询
5、通过抓包获取到我们的参数
'''
import requests as rs # 导包
# url = 'https://search.51job.com/list/020000,000000,0000,00,9,99,%25E6%25B5%258B%25E8%25AF%2595%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='
# headers = {
# "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
# }   # 现在需要headers里面的user-Agent，不然服务器会拦截你的请求
# r_51job = rs.get(url=url,headers=headers)
# # r_51job.encoding = 'gbk2312'       # 进行转码
# print(r_51job.encoding)     # 返回的是gbk，不需要转码，如果为乱码，可写：r_51job.encoding='gbk2312'
# print(r_51job.text)

# 发送请求需要cookies参数
'''
步骤：
1、打开12306的网站
2、打开12306的调试工具（一般默认快捷键是F12）
3、打开调试工具-选择network，进行抓包，如果原来里面有抓包信息，大家先清空下，点击clear
4、搜索车票，点击查询
5、通过抓包获取到我们的参数
'''
url_12306 = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2020-11-23&leftTicketDTO.from_station=DFZ&leftTicketDTO.to_station=SHH&purpose_codes=ADULT'
headers = {
'Cookie':'uab_collina=160082453269156416665244; JSESSIONID=DF72C0AB51A2AE3308D7D78879DCABDD; _jc_save_wfdc_flag=dc; BIGipServerotn=569377290.64545.0000; RAIL_EXPIRATION=1606403937323; RAIL_DEVICEID=OVPRUpMIvDT13kIzQ39f0o-j2gexkzqnj0XzQ6hpOjYYKWFINhzfDkO_SSzC3jQHOZgitmAmunDMd2of0FPxIR9npSBviFGMKeJNk6UpjoUVfzPVncycAKC2-gzh0_rdphI3bU-V9LcMyNAKCIzXyq8XfWwhTyX8; BIGipServerpool_passport=48497162.50215.0000; route=6f50b51faa11b987e576cdb301e545c4; _jc_save_fromStation=%u9053%u5DDE%2CDFZ; _jc_save_toStation=%u4E0A%u6D77%2CSHH; _jc_save_fromDate=2020-11-23; _jc_save_toDate=2020-11-23'
}
r_12306 = rs.get(url=url_12306,headers=headers)     # 不添加cookie，返回的编码是乱码
# r_12306.encoding = 'gbk2312'
print(r_12306.encoding)
print(r_12306.text) # 打印返回的结果