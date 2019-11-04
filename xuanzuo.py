# coding: utf-8

import time
from main import XuanZuo
from main import time_print
from main import get_time
from selenium.common.exceptions import NoSuchElementException

if __name__ == '__main__':
    xuanzuo = XuanZuo()
    time_print("等待57秒")
    time.sleep(57)
    while True:
        time_print("准备执行")
        timestamp = int(round(time.time() * 1000))
        xuanzuo.client.get("http://wechat.v2.traceint.com/index.php/prereserve/index.html")
        # print client.page_source
        try:
            title = xuanzuo.client.title
            if not title:
                time_print("cookie失效！！！")
                xuanzuo.save_screenshot("cookie失效")
                break
            site = xuanzuo.client.find_element_by_xpath("//tr/td[not(@class)]")
            # site = xuanzuo.client.find_element_by_xpath("//td[@class='disabled']")
            # //div[contains(@class,'grid_1')] 在自选座位界面选择一个可用的座位
            time_print("找到了座位：" + site.text)
            site.click()
            time_print("点击了：" + site.text)
            xuanzuo.save_screenshot("点击了座位按钮")
            tips = xuanzuo.client.find_element_by_id("ti_tips")
            time_print(tips.text)

        except NoSuchElementException as e:
            print e.msg
            try:
                text = xuanzuo.client.find_element_by_xpath("//h2[contains(text(),'不在预约时间内')]")
                time_print("不在预约时间内 " + str(int(round(time.time() * 1000)) - timestamp) + "ms")
            except NoSuchElementException as e:
                time_print("没有座位了！！！")
                xuanzuo.save_screenshot("没有座位了")
                break
        print "---------------------------------------"

    xuanzuo.close_clint()
