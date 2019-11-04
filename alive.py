# coding: utf-8
import time
from main import XuanZuo
from main import time_print

if __name__ == '__main__':
    xuanzuo = XuanZuo()
    while True:
        time_print("准备执行")
        timestamp = int(round(time.time() * 1000))
        xuanzuo.client.get("http://wechat.v2.traceint.com/index.php/prereserve/index.html")
        # print client.page_source

        title = xuanzuo.client.title
        if not title:
            print time_print("失败了")
            xuanzuo.save_screenshot("失败了")
            break
        time_print(title + " " + str(int(round(time.time() * 1000)) - timestamp) + "ms")
        print "-----------------------------------------"
        time.sleep(5 * 60)
    xuanzuo.client.quit()
