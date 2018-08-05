#-*- coding: utf-8 -*-
#发送附件
'''
如果Email中要加上附件怎么办？带附件的邮件可以看做包含若干部分的邮件：文本和各个附件本身，所以，可以构造一个MIMEMultipart对象代表邮件本身，然后往里面加上一个MIMEText作为邮件正文，再继续往里面加上表示附件的MIMEBase对象即可：
'''
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import smtplib

from_addr = '@qq.com'
password = ''
to_addr = '@163.com'
smtp_server = 'smtp.qq.com'

def _format_addr(s):
	name, addr = parseaddr(s)
	return formataddr((Header(name, 'utf-8').encode(), addr))
#邮件对象：
msg = MIMEMultipart()
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

#邮件正文是MIMEText：
msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))

#添加附件就是加上一个MIMEBse，从本地读取一个图片：
with open ('C:/Users/Hyunjia/Desktop/一寸头像/.jpg', 'rb') as f:
	#设置附件的MIME 和文件名，这里是jpg类型：
	mime = MIMEBase('image', 'jpg', filename='.jpg')
	#加上必要的头信息
	mime.add_header('Content-Disposition', 'attachment',filename='.jpg')
	mime.add_header('Content-ID', '<0>')
	mime.add_header('X-Atachment-Id', '0')
	#把附件的内容读进来
	mime.set_payload(f.read())
	#用Base64编码
	encoders.encode_base64(mime)
	#添加到MIMEMultipart：
	msg.attach(mime)



server = smtplib.SMTP_SSL(smtp_server, 465)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
print('发送成！！！')
server.quit()