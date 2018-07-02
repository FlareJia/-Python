# -*- coding: utf-8 -*-
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
d['Michael']

da['Adam'] = 67
da['Adam']

'Thomas' in da

d.get('Thomas')

d.get('Thomas', -1)

d.pop('Bob')
d


#set无序，重复元素在set中自动被过滤：
s = set([1, 2, 3])
s

s = set([1, 1, 2, 2, 3, 3])
s

#通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果：
s.add(4)
s
s.add(4)
s

#remove(key)方法可以删除元素:
s.remove(4)
s
#两个set可以做数学意义上的交集、并集等操作：
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
s1 & s2
s1 | s2

#对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的。
