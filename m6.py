#-*- coding: utf-8 -*-
import socket
'''
recvfrom()方法返回数据和客户端的地址与端口，这样，服务器收到数据后，直接调用sendto()就可以把数据用UDP发给客户端。

注意这里省掉了多线程，因为这个例子很简单。

客户端使用UDP时，首先仍然创建基于UDP的Socket，然后，不需要调用connect()，直接通过sendto()给服务器发数据：
'''
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in [b'Michael', b'Tracy', b'Flare']:
	#发送数据：
	s.sendto(data,('127.0.0.1', 9999))
	#接收数据：
	print(s.recv(1024).decode('utf-8'))
s.close()
'''
从服务器接收数据仍然调用recv()方法。

仍然用两个命令行分别启动服务器和客户端测试，结果如下：
'''
