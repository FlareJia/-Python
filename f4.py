#-*- coding: utf-8 -*-
#当我们拿到一个对象的引用时，如何知道这个对象是什么类型、有哪些方法呢？
#用type()

type(123)




#判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量：

#>>> import types
#>>> def fn():
#...     pass
#...
#>>> type(fn)==types.FunctionType
#True
#>>> type(abs)==types.BuiltinFunctionType
#True
#>>> type(lambda x: x)==types.LambdaType
#True
#>>> type((x for x in range(10)))==types.GeneratorType



#使用isinstance()
#对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。

#并且还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple：

#>>> isinstance([1, 2, 3], (list, tuple))
#True
#>>> isinstance((1, 2, 3), (list, tuple))
#True

#!!!!!!!!!! 总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。

#使用dir()
#如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：

#我们自己写的类，如果也想用len(myObj)的话，就自己写一个__len__()方法：

#>>> class MyDog(object):
#...     def __len__(self):
#...         return 100
#...
#>>> dog = MyDog()
#>>> len(dog)
#100

class Student(object):
	count=0
	def __init__(self,name):
		self.name=name
		Student.count+=1


# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败1!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败2!')
        else:
            print('Students:', Student.count)
            print('测试通过!')