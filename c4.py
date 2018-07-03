#那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。
#-*- coding: utf-8 -*-
#要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：

g=(x*x for x in range(10))
print(g)

#创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator。



#我们可以直接打印出list的每一个元素，但我们怎么打印出generator的每一个元素呢？
#如果要一个一个打印出来，可以通过next()函数获得generator的下一个返回值：

#我们讲过，generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误。
#将所有打印出来
print(next(g))

for n in g:
	print(n)
	
print('\n')
#斐波拉契数列用列表生成式写不出来，但是，用函数把它打印出来却很容易：
def fib(max):
	n,a,b=0,0,1
	while n<max:
		yield(b)
		a,b=b,a+b
		n=n+1
	return 'done'


#要把fib函数变成generator，只需要把print(b)改为yield b就可以了：
#这就是定义generator的另一种方法。如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：

#这里，最难理解的就是generator和函数的执行流程不一样。
#函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
#而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。


def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)

o=odd()
next(o)
next(o)
next(o)

for i in fib(6):
	print(i)

#但是用for循环调用generator时，发现拿不到generator的return语句的返回值。如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：

g=fib(6)
while True:
	try:
		x=next(g)
		print('g:',x)
	except StopIteration as e:
		print('Generator return value',e.value)
		break
		
		
#练习
#杨辉三角
def triangles():
	L2=[0]
	L=[1]
	while True:
		yield L
		L1=L
		L=[1]
		for i in range(len(L2)+1):
			if i==0:
				continue
			elif i==len(L2):
				L.append(1)
			else:
				L.append(L1[i]+L1[i-1])
		L2.append(0)
	return 'done'

# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')		
	
#虽然成功了，但是评论那里有更简洁的写法，下次记得去看！！！！