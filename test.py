# coding=utf-8
from main import XuanZuo, time_print
import time

xuanzuo = XuanZuo()
time_print("准备执行")
timestamp = int(round(time.time() * 1000))
xuanzuo.client.get("http://wechat.v2.traceint.com/index.php/prereserve/index.html")
# print client.page_source

print xuanzuo.client.title
xuanzuo.save_screenshot("test_charset")
xuanzuo.close_clint()
