# coding: utf-8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import sys
import os
import pytz

reload(sys)
sys.setdefaultencoding('utf8')

session_id = "0ca7142aa291f0c5fe5c13db165a66d4ef49fc2664d32057"


class XuanZuo:
    def __init__(self):
        print("启动一个客户端")
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--remote-debugging-port=9222')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument("user-agent='Mozilla/5.0 (Linux; Android 10; MIX 2S Build/QKQ1.190828.002; wv) "
                                    "AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 "
                                    "MQQBrowser/6.2 "
                                    "TBS/44940 Mobile Safari/537.36 MMWEBID/4668 MicroMessenger/7.0.7.1521(0x27000735) "
                                    "Process/tools NetType/WIFI Language/zh_CN'")

        self.client = webdriver.Chrome(chrome_options=chrome_options,
                                       executable_path='/Users/fujie/chromedriver')
        print("客户端启动完成")
        self.client.get("http://wechat.v2.traceint.com")
        self.client.add_cookie({
            'domain': 'wechat.v2.traceint.com',
            'name': 'wechatSESS_ID',
            'value': session_id,
            'path': '/',
            'expires': None
        })

    def close_clint(self):
        self.client.quit()

    def save_screenshot(self, title):
        self.client.save_screenshot(os.path.abspath(os.path.dirname(__file__)) +
                                    "/result/" + title + "-" + get_time() + ".png")


def get_time():
    return datetime.now(pytz.timezone("Asia/Shanghai")).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]


def time_print(text):
    print get_time() + ": " + str(text)


