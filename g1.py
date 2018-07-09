#-*- coding: utf-8 -*-
#有没有既能检查参数，又可以用类似属性这样简单的方式来访问类的变量呢？对于追求完美的Python程序员来说，这是必须要做到的！

#还记得装饰器（decorator）可以给函数动态加上功能吗？对于类的方法，装饰器一样起作用。Python内置的@property装饰器就是负责把一个方法变成属性调用的：



#@property的实现比较复杂，我们先考察如何使用。把一个getter方法变成属性，只需要加上@property就可以了，此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作：
#意到这个神奇的@property，我们在对实例属性操作的时候，就知道该属性很可能不是直接暴露的，而是通过getter和setter方法来实现的。

#还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：
#上面的birth是可读写属性，而age就是一个只读属性，因为age可以根据birth和当前时间计算出来。


#小结

#@property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性。


#练习
class Screen(object):
	@property
	def width(self):
		return self._width
	
	@width.setter
	def width(self,width):
		self._width=width
	
	@property
	def height(self):
		return self._height
	
	@height.setter
	def height(self,height):
		self._height=height
	
	@property
	def resolution(self):
		return 786432
		
# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')