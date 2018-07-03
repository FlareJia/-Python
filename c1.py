#-*- coding: utf-8 -*-
L=['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

#取前三个元素
#笨方法一，用循环
r=[]
n=3
for i in range(n):
	r.append(L[i])

print(r)

#方法二，用切片,从0开始，取到索引3为止，但不包括3
#如果第一个索引是0，还可以省略：
print(L[0:3])
#python支持取倒数的元素
print(L[-2])
#从倒数第二个开始，取到倒数第一个,但不包括倒数第一个
print(L[-2:-1])

L1=list(range(100))
print(L1)

#取出前十个数
print(L1[:10])
#取后十个数
print(L1[-10:])

#取前11-20个数
print(L1[10:20])

print(r'前十个数，每两个取一个')
print(L1[:10:2])

print(r'所有数，每五个取一个')
print(L1[::5])

#甚至什么都不写，只写[:]就可以原样复制一个list

print(r'tuple也是一种list，唯一区别是tuple不可变，它也可以用切片操作，只是操作结果若是tuple')
print(r"字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串：")



print('练习：')
def trim1(s):
	n=-1
	m=len(s)-1
	for i in s:
		if i.isspace():
			m=m+1
	for i in s:
		n=n+1
		if not i.isspace():
			break
	print(s[-7:-1])
	for i in s[-7:-1]:
		m=m-1
		if not i.isspace():
			break
	print(s[n:m])
	print('n',n,'m',m)
	return s[n:m]
	
#5555....这是别人的答案 递归
def trim(s):
	if s[:1]==' ':
		return trim(s[1:])
	elif s[-1:]==' ':
		return trim(s[:-1])
	else:
		return s
# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!1')
elif trim('  hello') != 'hello':
    print('测试失败!2')
elif trim('  hello  ') != 'hello':
    print('测试失败!3')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!4')
elif trim('') != '':
    print('测试失败!5')
elif trim('    ') != '':
    print('测试失败!6')
else:
    print('测试成功!')