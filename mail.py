# coding=utf-8
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from main import time_print, cur_path


class MyQQEmail:
    def __init__(self):
        self.stmpObj = smtplib.SMTP_SSL("smtp.qq.com", 465)
        self.stmpObj.login("fujie.me", "授权码")

    def send_mail(self, sender, receivers, subject, msg, image_file_name=None):
        message = MIMEMultipart('related')
        message['Subject'] = Header("【抢座】" + subject, 'utf-8')
        message['From'] = sender
        message['To'] = ",".join(receivers)
        msgAlternative = MIMEMultipart('alternative')
        message.attach(msgAlternative)

        mail_msg = '<p>' + msg + '</p>'

        if image_file_name is not None:
            # 指定图片为当前目录
            fp = open(cur_path + "/result/" + image_file_name, 'rb')
            msgImage = MIMEImage(fp.read())
            fp.close()

            # 定义图片 ID，在 HTML 文本中引用
            msgImage.add_header('Content-ID', '<image1>')
            message.attach(msgImage)
            mail_msg += '<p>结果截图：</p> <p><img src="cid:image1"></p>'

        msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))

        try:
            self.stmpObj.sendmail(sender, receivers, message.as_string())
            time_print("邮件发送成功")
        except smtplib.SMTPException as e:
            time_print("邮件发送失败")
            print e


if __name__ == '__main__':
    mail = MyQQEmail()
    mail.send_mail("fujie.me@qq.com", ["fujie@xiyoulinux.org", "1014810037@qq.com"], "测试标题", "测试内容", "没有座位了-2019-11-05 22:53:20.651.png")
