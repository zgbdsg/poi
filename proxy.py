# -*- coding: utf-8 -*-
import execjs
import re
import requests
from bs4 import BeautifulSoup
import random
import time

url = "http://www.kuaidaili.com/free/inha/1/"

HERDERS = {
    "Host": "www.kuaidaili.com",
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36',
}


def executejs(html):
    # 提取其中的JS加密函数
    js_string = ''.join(re.findall(r'(function .*?)</script>',html))

    # 提取其中执行JS函数的参数
    js_func_arg = re.findall(r'setTimeout\(\"\D+\((\d+)\)\"', html)[0]
    js_func_name = re.findall(r'function (\w+)',js_string)[0]

    # 修改JS函数，使其返回Cookie内容
    js_string = js_string.replace('eval("qo=eval;qo(po);")', 'return po')

    func = execjs.compile(js_string)
    return func.call(js_func_name,js_func_arg)

def parse_cookie(string):
    string = string.replace("document.cookie='", "")
    clearance = string.split(';')[0]
    return {clearance.split('=')[0]: clearance.split('=')[1]}

# 第一次访问获取动态加密的JS
first_html = requests.get(url=url,headers=HERDERS).content.decode('utf-8')

# 执行JS获取Cookie
cookie_str = executejs(first_html)

# 将Cookie转换为字典格式
cookie = parse_cookie(cookie_str)
print('cookies = ',cookie)

# 带上cookies参数，再次请求
urlformat = "http://www.kuaidaili.com/free/intr/%d/"
f = open('ip.csv','w')

for i in xrange(1, 1000):
    url = urlformat%i
    response = requests.get(url=url,headers=HERDERS,cookies=cookie)
    #print response.text
    soup = BeautifulSoup(response.text)
    for tr in soup.find_all('tr'):
        tds = tr.find_all('td')
        if len(tds) > 2:
            #print tds[0].string, tds[1].string
            raw_proxy = "%s:%s"%(tds[0].string, tds[1].string)
            proxies = {"http": "http://{proxy}".format(proxy=raw_proxy)}
            try:
                r = requests.get('http://www.baidu.com/', proxies=proxies, timeout=10, verify=False)
                if r.status_code == 200:
                    f.write("%s,%s\n"%(tds[0].string, tds[1].string), 1)
                    print raw_proxy,'success'
            except Exception, e:
                print raw_proxy,'fail'
                pass

    time.sleep(random.randint(1,5))



