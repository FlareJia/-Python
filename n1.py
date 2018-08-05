#-*- coding: utf-8 -*-
'''
SMTP是发送邮件的协议，Python内置对SMTP的支持，可以发送纯文本邮件、HTML邮件以及带附件的邮件。

Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件。

首先，我们来构造一个最简单的纯文本邮件：
'''
import smtplib
from email.mime.text import MIMEText

'''
#注意到构造MIMEText对象时，第一个参数就是邮件正文，第二个参数是MIME的subtype，传入'plain'表示纯文本，最终的MIME就是'text/plain'，最后一定要用utf-8编码保证多语言兼容性。

#然后，通过SMTP发出去：
'''
#输入Email地址和口令：
from_addr = "@qq.com"
password = ""


#输入收件人地址：
to_addr = "@163.com"

#输入SMTP服务器地址：
smtp_server = "smtp.qq.com"

msg = MIMEText('hello, send by Python...5 to w', 'plain', 'utf-8')

server = smtplib.SMTP_SSL(smtp_server, 465) #SMTP协议默认端口是25

server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, to_addr, msg.as_string())
print("mail has been send successfully.")
server.quit()
'''
#我们用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息。SMTP协议就是简单的文本命令和响应。login()方法用来登录SMTP服务器，sendmail()方法就是发邮件，由于可以一次发给多个人，所以传入一个list，邮件正文是一个str，as_string()把MIMEText对象变成str。
'''



'''
def send_email(smtpHost, sendAddr, password, recipientAddrs, subject='', content=''):
	msg = email.mime.multipart,MIMEMultipart()
	msg['from'] = sendAddr
	msg['to'] = recipientAddrs
	msg['subject'] = subject
	content = content
	txt = email.mime.text.MIMEText(content, 'plain', 'utf-8')
	msg.attach(txt)
	
	smtp = smtplib.SMTP()
	smtp.connect(smtpHost, '25')
	smtp.login(sendAddr, password)
	smtp.sendmail(sendAddr, recipientAddrs, str(msg))
	print('发送成功！！！')
	smtp.quit()
	

subject = 'Python test'
content = ' 从python发的邮件'
send_email('smtp.qq.com', '@qq.com', '', '@163.com', subject, content)
'''