#���ڵ����ַ��ı��룬Python�ṩ��ord()������ȡ�ַ���������ʾ��chr()�����ѱ���ת��Ϊ��Ӧ���ַ���
#>>> ord('A')
#65
#>>> ord('��')
#20013
#>>> chr(66)
#'B'
#>>> chr(25991)
#'��'

#>>> 'ABC'.encode('ascii')
#b'ABC'
#>>> '����'.encode('utf-8')
#b'\xe4\xb8\xad\xe6\x96\x87'
#>>> '����'.encode('ascii')
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)

#��bytes�У��޷���ʾΪASCII�ַ����ֽڣ���\x##��ʾ��


#���bytes�а����޷�������ֽڣ�decode()�����ᱨ��

#>>> b'\xe4\xb8\xad\xff'.decode('utf-8')
#Traceback (most recent call last):
# ...
#UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 3: invalid start byte
#���bytes��ֻ��һС������Ч���ֽڣ����Դ���errors='ignore'���Դ�����ֽڣ�

#>>> b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')
#'��'







#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#��һ��ע����Ϊ�˸���Linux/OS Xϵͳ������һ��Python��ִ�г���Windowsϵͳ��������ע�ͣ�
#�ڶ���ע����Ϊ�˸���Python������������UTF-8�����ȡԴ���룬��������Դ������д������������ܻ������롣
