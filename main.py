# coding: utf-8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import sys
import os
import pytz
import time

reload(sys)
sys.setdefaultencoding('utf8')

cur_path = os.path.abspath(os.path.dirname(__file__))


class XuanZuo:
    def __init__(self):
        time_print("启动一个客户端")
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
                                       executable_path=cur_path +
                                                       '/driver/chromedriver')
        time_print("客户端启动完成")
        self.set_cookie()

    def set_cookie(self):
        time_print("更新cookie")
        self.client.delete_all_cookies()
        self.client.get("http://wechat.v2.traceint.com")
        with open(cur_path + "/session.txt") as f:
            session_id = f.read().strip()
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
        self.client.save_screenshot(cur_path +
                                    "/result/" + title + "-" + get_time() + ".png")


def get_time():
    return datetime.now(pytz.timezone("Asia/Shanghai")).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]


def time_print(text, timestamp=None):
    if timestamp:
        print get_time() + ": " + str(text) + " " + str(int(round(time.time() * 1000)) - timestamp) + "ms"
    else:
        print get_time() + ": " + str(text)


def get_ms_timestamp():
    return int(round(time.time() * 1000))


if __name__ == '__main__':
    xuanz = XuanZuo()
    print xuanz.client.get_cookies()
    import time
    time.sleep(30)
    xuanz.set_cookie()
    print xuanz.client.get_cookies()
