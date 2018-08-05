#-*- coding: utf-8 -*-

'''
连接建立后，服务器首先发一条欢迎消息，然后等待客户端数据，并加上Hello再发送给客户端。如果客户端发送了exit字符串，就直接关闭连接。

要测试这个服务器程序，我们还需要编写一个客户端程序：
我们需要打开两个命令行窗口，一个运行服务器程序，另一个运行客户端程序，就可以看到效果了
'''
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#建立连接：
s.connect(('127.0.0.1', 9999))
#接收欢迎消息
print(s.recv(1024).decode('utf-8'))
for data in [b'Michael', b'Tracy', b'Flare']:
	#发送数据：
	s.send(data)
	print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()
