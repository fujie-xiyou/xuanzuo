# coding: utf-8

import time
from main import XuanZuo
from main import time_print
from main import get_time
from selenium.common.exceptions import NoSuchElementException

if __name__ == '__main__':
    xuanzuo = XuanZuo()
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
            # //div[contains(@class,'grid_1')] 在自选座位界面选择一个可用的座位
            time_print(title)
            site.click()
            tips = xuanzuo.client.find_element_by_id("ti_tips")
            time_print(tips.text)
            xuanzuo.save_screenshot("成功")

        except NoSuchElementException as e:
            try:
                text = xuanzuo.client.find_element_by_xpath("//h2[contains(text(),'不在预约时间内')]")
                time_print("不在预约时间内")
            except NoSuchElementException as e:
                time_print("没有座位了！！！")
                xuanzuo.save_screenshot("没有座位了")
                break
        print "---------------------------------------"

    xuanzuo.close_clint()
