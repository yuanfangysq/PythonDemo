#!/usr/bin/env python3
# -*- coding: utf-8 -*-



__author__ = 'ysq'

import sys
#保存图片
from PIL import Image
im = Image.open('test.png')
print(im.format, im.size, im.mode)
im.thumbnail((2000, 1000))
im.save('ym2.jpg', 'JPEG')
print(sys.argv)
print(sys.path)
print('当前系统是:',sys.platform)
d = {'a': 1, 'b': 2, 'c': 3}
for key in d.values():
	print(key)
print([x * x for x in range(1, 11) if x == 10][0])
g = (x2 * x2 for x2 in range(10))
print(next((x2 * x2 for x2 in range(10))))
def f(x):
	return x*x-1
	pass
#函数参数为函数
r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))
#end
#函数返回类型是某个函数(闭包或者说bloke)
def ysq_sum(c,*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax+c
    return sum
hs=ysq_sum(11,*list(range(10)))
print(hs(),'是个block')
#简单的闭包
# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():
#              return i*i
#         fs.append(f)
#     return fs
#难点的闭包
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs
f1 = count()
print(f1[1]())
#返回一个匿名函数
def build(x, y):
    return lambda: x * x + y * y
niming = build(2,2)
print('匿名函数',niming())
def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')
if __name__=='__main__':
    test()
#私有的方法
def _private_1(name):
	return 'Hello, %s' % nam

for k,v in d.items():
	print(k,v)
