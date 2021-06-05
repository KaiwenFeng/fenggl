# coding: utf-8
"""
1、配合万网的域名查询接口
2、python38实现批量查询指定长度的字母数字域名是否被注册
3、使用笛卡尔积实现排列组合拼接域名
4、因为接口请求有限制，就不用多线程来速战速决了
"""

import time
import string
import logging
import requests
import itertools
from xml.etree import ElementTree as ET

"""
- returncode=200 表示接口返回成功 
- key=*.com表示当前check的域名 
- original=210 : Domain name is available 表示域名可以注册 
- original=211 : Domain name is not available 表示域名已经注册 
- original=212 : Domain name is invalid 表示域名参数传输错误 
- original=213 : Time out 查询超时
"""

logging.basicConfig(level=logging.INFO,
    format='[%(asctime)s] %(filename)s(line:%(lineno)d) %(levelname)s - %(message)s',
    datefmt='%a, %d %b %Y %H:%M:%S',
    filename='domain.log')

domain_check_api = "http://panda.www.net.cn/cgi-bin/check.cgi?area_domain={}"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}


def write_file(domain):
    with open("domain.txt", "a+") as f:
        f.write(f"{domain}\n")


def req_data(domain):
    try:
        result = requests.get(domain_check_api.format(domain), headers=headers)
        root = ET.XML(result.text)
        for node in root.iter('property'):
            code = node.find('returncode').text
            original = node.find('original').text
            if int(code) == 200 and '210' in original:
                write_file(domain)
                print(f"[{domain}]可注册")
            else:
                logging.info(f"[{code}][{original}][{domain}]不可注册")
        time.sleep(0.1)
    except:
        pass


def main(sd, domain_length, domain_suffix):
    for ds in domain_suffix:
        for x in itertools.product(sd, repeat = domain_length):
            domain = f"{''.join(x)}.{ds}"
            req_data(domain)


if __name__ == "__main__":
    # sd = string.digits    # 纯数字
    sd = string.ascii_lowercase # 纯字母
    sd = 'fengkaiwenjun'
    # sd = string.digits+string.ascii_lowerhttps://pi.app/voutubecase # 数字字母组合
    domain_length = 4
    domain_suffix = ['com']
    main(sd, domain_length, domain_suffix)
