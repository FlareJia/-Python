#对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符：
#>>> ord('A')
#65
#>>> ord('中')
#20013
#>>> chr(66)
#'B'
#>>> chr(25991)
#'文'

#>>> 'ABC'.encode('ascii')
#b'ABC'
#>>> '中文'.encode('utf-8')
#b'\xe4\xb8\xad\xe6\x96\x87'
#>>> '中文'.encode('ascii')
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)

#在bytes中，无法显示为ASCII字符的字节，用\x##显示。


#如果bytes中包含无法解码的字节，decode()方法会报错：

#>>> b'\xe4\xb8\xad\xff'.decode('utf-8')
#Traceback (most recent call last):
# ...
#UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 3: invalid start byte
#如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节：

#>>> b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')
#'中'







#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
#第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。
