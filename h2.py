#-*- coding: utf-8 -*-
#调试
#用print()最大的坏处是将来还得删掉它，想想程序里到处都是print()，运行结果也会包含很多垃圾信息。所以，我们又有第二种方法。


#断言

#凡是用print()来辅助查看的地方，都可以用断言（assert）来替代：

def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('0')
	
#assert的意思是，表达式n != 0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错。
#如果断言失败，assert语句本身就会抛出AssertionError：


#程序中如果到处充斥着assert，和print()相比也好不到哪去。不过，启动Python解释器时可以用-O参数来关闭assert：
#在命令行这样输入：$ python -O err.py
#关闭后，你可以把所有的assert语句当成pass来看。



#把print()替换为logging是第3种方式，和assert比，logging不会抛出错误，而且可以输出到文件：
#logging.info('n=%d' % n)
