# coding: utf-8
import time

from mail import MyQQEmail
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
            file_name = xuanzuo.save_screenshot("cookie过期")
            mailObj = MyQQEmail()
            mailObj.send_mail("fujie.me@qq.com",
                              ["fujie@xiyoulinux.org", "2931501182@qq.com", "907071163@qq.com"],
                              "cookie过期！", "cookie过期，请及时更新", file_name)
            mailObj.stmpObj.quit()
            break
        time_print(title, timestamp)
        print "-" * 40
        try:
            time.sleep(15 * 60)
        except KeyboardInterrupt as e:
            time_print("手动终止 %s" % e)
            break
        except Exception as e:
            time_print("异常终止：%s" % e)
            break
    print "-" * 40
    xuanzuo.client.quit()
