#-*- coding: utf-8 -*-

#map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
def f(x):
	return x*x

r=map(f,[1,2,3,4,5,6,7,8,9])
print(list(r))
#map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。

#map()作为高阶函数，事实上它把运算规则抽象了，因此，我们不但可以计算简单的f(x)=x2，还可以计算任意复杂的函数，比如，把这个list所有数字转为字符串：
print(list(map(str,[1,2,3,4,5,6,7,8,9])))

#再看reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
#reduce(f,[x1,x2,x3,x4])=f(f(f(x1,x2),x3),x4)


#比方说对一个序列求和，就可以用reduce实现：
from functools import reduce
def add(x,y):
	return x+y
	
print(reduce(add,[1,3,5,7,9]))

#但是如果要把序列[1, 3, 5, 7, 9]变换成整数13579，reduce就可以派上用场：
def fn(x,y):
	return x*10+y

print(reduce(fn,[1,3,5,7,9]))


#这个例子本身没多大用处，但是，如果考虑到字符串str也是一个序列，对上面的例子稍加改动，配合map()，我们就可以写出把str转换为int的函数：
def char2num(s):
	digits={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'0':0}
	return digits[s]

print(reduce(fn,map(char2num,'13579')))

#整理成一个strtoint的函数就是：
DIGITS={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'0':0}
def strtoint(s):
	def fn(x,y):
		return x*10+y
	def char2num(s):
		return DIGITS[s]
	return reduce(fn,map(char2num,s))
	
#还可以用lambda函数进一步简化成：

def newchar2num(s):
	return DIGITS[s]

def newstr2int(s):
	return reduce(lambda x,y:x*10+y,map(newchar2num,s))

#也就是说，假设Python没有提供int()函数，你完全可以自己写一个把字符串转化为整数的函数，而且只需要几行代码！


#练习1：
def normalize(name):
	a=name[0:1]
	b=name[1:]
	return a.upper()+b.lower()
	

#测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

#练习2：
def prod(L):
	def multi(x,y):
		return x*y
	return reduce(multi,L)

#测试：
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')
	
#练习3：

def str2float(s):
	digits={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'0':0,'.':0.1}
	flag=0
	L1=[]
	L2=['0']
	for i in s:
		if i=='.':
			flag=1
		elif flag==0:
			L1.append(i)
		else:
			L2.append(i)
#	def reverse(l):
#		u=n=len(l)
#		for i in range(n):
#			if i>=n/2:
#				break
#			else:	
#				t=l[i]
#				l[i]=l[u-1]
#				l[u-1]=t
#				u=u-1
#				print('newL2:',L2)
#		return l
	print('L1:',L1)
	print('L2:',L2)
#	reverse(L2)
	def str2num(l):
		return digits[l]
	def merge1(x,y):
		return x*10+y
	def merge2(x,y):
		return x*0.1+y	
	a=reduce(merge1,map(str2num,L1))
	print(a)
	b=reduce(merge2,map(str2num,L2[::-1]))
	print(b)
	return a+b
			

#测试：
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')