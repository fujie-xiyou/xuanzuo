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
            print time_print("cookie过期")
            xuanzuo.save_screenshot("cookie过期")
            xuanzuo.set_cookie()
        time_print(title, timestamp)
        print "-" * 40
        try:
            time.sleep(15 * 60)
        except KeyboardInterrupt as e:
            xuanzuo.client.quit()
            print "手动终止"
            break
