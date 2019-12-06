# coding: utf-8

import time
from datetime import datetime, date, timedelta
from main import XuanZuo
from main import time_print
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from mail import Email

if __name__ == '__main__':
    mailObj = Email("smtp.qq.com", 465, "fujie.me", "授权码")
    xuanzuo = XuanZuo()
    try:
        d = date.today()
        eight = datetime(d.year, d.month, d.day) + timedelta(hours=8)
        stamp = time.mktime(eight.timetuple())
        sec = stamp - time.time() - 1
        time_print("等待%s秒" % sec)
        time.sleep(sec)
        while True:
            time_print("准备执行")
            timestamp = int(round(time.time() * 1000))
            xuanzuo.client.get("http://wechat.v2.traceint.com/index.php/prereserve/index.html")
            # print client.page_source
            if len(xuanzuo.client.find_elements_by_xpath("//h2[contains(text(),'不在预约时间内')]")) > 0:
                time_print("不在预约时间内", timestamp)
                print "-" * 40
                continue
            if len(xuanzuo.client.find_elements_by_xpath("//h2[contains(text(),'你已经预定了明天')]")) > 0:
                time_print("已经预定过了！", timestamp)
                print "-" * 40
                break
            title = xuanzuo.client.title
            if not title:
                time_print("cookie失效！！！")
                xuanzuo.save_screenshot("cookie失效")
                break
            site = xuanzuo.client.find_element_by_xpath("//tr/td[not(@class)]")
            # site = xuanzuo.client.find_element_by_xpath("//td[@class='disabled']")
            # //div[contains(@class,'grid_1')] 在自选座位界面选择一个可用的座位
            time_print("找到了座位：" + site.text + " " + str(int(round(time.time() * 1000)) - timestamp) + "ms")
            timestamp = int(round(time.time() * 1000))
            site.click()
            time_print("点击了：" + site.text + " " + str(int(round(time.time() * 1000)) - timestamp) + "ms")
            xuanzuo.save_screenshot("点击了座位按钮")
            timestamp = int(round(time.time() * 1000))
            tips = WebDriverWait(xuanzuo.client, 2, 0.1).until(EC.presence_of_element_located((By.ID, "ti_tips")))
            time_print(tips.text, timestamp)
            file_name = xuanzuo.save_screenshot(tips.text)
            if tips.text == "预定座位成功":
                mailObj.send_mail("fujie.me@qq.com",
                                  ["fujie@xiyoulinux.org", "2931501182@qq.com", "907071163@qq.com"],
                                  tips.text, "成功预订了：" + site.text, file_name)

                print "-" * 40
                break

    except NoSuchElementException as e:
        print e.msg
        time_print("没有座位了！！！")
        file_name = xuanzuo.save_screenshot("没有座位了")
        mailObj.send_mail("fujie.me@qq.com",
                          ["fujie@xiyoulinux.org", "907071163@qq.com"],
                          "抢座失败！", "没有座位了。。", file_name)

    except IOError as e:
        print "出错了"
        print e
        mailObj.send_mail("fujie.me@qq.com",
                          ["fujie@xiyoulinux.org", "907071163@qq.com"],
                          "出错了", "错误信息：<br/>" + str(e))

    print "-" * 40

    xuanzuo.close_clint()
    mailObj.stmpObj.quit()
