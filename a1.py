a = 100
if a >= 0:
    print(a)
else:
    print(-a)
    
print('''line1
line2
line3''')
#多行字符串'''...'''还可以在前面加上r使用:
print(r'''hello,\n
world''')
print(True,'\n')
print(False,'\n')
print('3>2=')
print(3>2,'\n')
print('3>5=')
print(3>5,'\n')
print('not True=')
print(not True,'\n')

age=19
if age>=18:
	print('adult')
	print('im',age,'years old.')
else:
	print('teeager')
#空值是Python里一个特殊的值，用None表示。None不能理解为0，因为0是有意义的，而None是一个特殊的空值。


a=123 #a是整数
print(a)
a='ABC'#a变为字符串
print(a)
a="abc  %%"
print(a)

x=10
x=x+2
print(x,'\n')

#这玩意儿有点像C语言
print('''a='ABC'
b=a
a='XYZ'
''')
a='ABC'
b=a
a='XYZ'
print(b)

#/除法计算结果是浮点数，即使是两个整数恰好整除，结果也是浮点数：
print('10/3=')
print(10/3)
print('9/3=')
print(9/3)

#还有一种除法是//，称为地板除，两个整数的除法仍然是整数,只取整数部分
print('10//3=')
print(10//3)

#练习
n=123
f=456.789
s1='Hello,world'
s2='Hello,\'Adam\''
s3=r'Hello,"Bart"'
s4=r'''Hello,Lisa!'''
print(n,f,s1,s2,s3,s4)