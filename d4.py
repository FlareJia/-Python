#-*- coding: utf-8 -*-
#如果不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？可以不返回求和的结果，而是返回求和的函数：
def lazy_sum(*args):
	def sum():
		ax=0
		for n in args:
			ax=ax+n
		return ax
	return sum

#当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数：
f=lazy_sum(1, 3, 5, 7, 9)
print(f)
#调用函数f时，才真正计算求和的结果：
print(f())

#请再注意一点，当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：
#在这个例子中，我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。

#!!!!!!!!返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。!!!!!!!!!!

#练习
#利用闭包返回一个计数器函数，每次调用它返回递增整数：
def createCounter():
    n=0
    def counter():
        nonlocal n  #nonlocal关键字用来在函数或其他作用域中使用外层(非全局)变量。
        n+=1
        return n
    return counter

# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')