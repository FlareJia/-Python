# -*- coding：utf-8 -*-

def power(x,n=2):
	s=1
	while n>0:
		n=n-1
		s=s*x
	return s

#一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；
#当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
#也可以不按顺序提供部分默认参数。当不按顺序提供部分默认参数时，需要把参数名写上。	
def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

enroll('Bob', 'M', 7)
enroll('Adam', 'M', city='Tianjin')

#默认参数很有用，但使用不当，也会掉坑里。默认参数有个最大的坑，演示如下：
def add_end(L=[]):
    L.append('END')
    return L
	
#正常
add_end([1,2,3])
#正常
add_end(['x','y','z'])
#正常
add_end()
#不正常
add_end()
#不正常
add_end()
#原因解释如下：

#Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，
#因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。

#定义默认参数要牢记一点：默认参数必须指向不变对象！！！！！！！！！！！！！！！！！！！！！！

def add_endnew(L=None):
	if L is None:
		L=[]
	L.append('END')
	return L
	
	
	
#可变参数
def calc(*numbers):
	sum=0
	for n in numbers:
		sum=sum+n*n
	return sum
#定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。
#在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数

#如果已经有一个list或者tuple，要调用一个可变参数怎么办？可以这样做：
nums = [1, 2, 3]
calc(nums[0], nums[1], nums[2])

#这种写法当然是可行的，问题是太繁琐，所以Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去：
calc(*nums)

def person(name,age,**kw):
	print('name',name,'age',age,'other:',kw)

#函数person除了必选参数name和age外，还接受关键字参数kw。在调用该函数时，可以只传入必选参数：
#也可以传入任意个数的关键字参数
person('Bob',35,city='Beijing')
person('Adam',45,gender='M',job='Engineer')

#上面的简单写法：
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)

#如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
def person(name, age, *, city, job):
    print(name, age, city, job)

#和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。

#命名关键字参数可以有缺省值，从而简化调用
def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)

#！！！！！！！！！！参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。



def product(a,*n):
	s=a
	for num in n:
		s=s*num
	return s
		
# 测试
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!1')
elif product(5, 6) != 30:
    print('测试失败!2')
elif product(5, 6, 7) != 210:
    print('测试失败!3')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!4')
else:
    try:
        product()
        print('测试失败!5')
    except TypeError:
        print('测试成功!')