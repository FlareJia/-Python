#-*- coding: utf-8 -*-
#迭代
#dic也可迭代
d={'a': 1, 'b': 2, 'c': 3}
for key in d:
	print(key)

#因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样。
#默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.values()，如果要同时迭代key和value，可以用for k, v in d.items()。


#那么，如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：
from collections import Iterable
print(isinstance('abc',Iterable))
print(isinstance([1,2,3],Iterable))
print(isinstance(123,Iterable))

#如果要对list实现类似Java那样的下标循环怎么办？Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
for i,value in enumerate(['A','B','C']):
	print(i,value)

#for中有两个变量，很常见
for x, y in [(1, 1), (2, 4), (3, 9)]:
	print(x, y)
	
#练习
def findMinAndMax(L):
	if len(L)==0:
		return (None,None)
	else:
		min=L[0]
		max=L[0]
		for x in L:
			if x<min:
				min=x
			elif x>max:
				max=x
	return (min,max)

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')