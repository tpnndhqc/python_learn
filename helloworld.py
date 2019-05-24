# -*- coding: UTF-8 -*
#或者# coding=utf-8

# # 函数名其实就是指向函数的变量！
# f = abs
# print(f(-10))
#
# # 函数的参数能够接收别的函数，这种函数就称之为高阶函数。
# def add(x, y, f):
#     return f(x) + f(y)
# print(add(-5, 6, abs))
#
# # Python内建了map()和reduce()函数。
'''
map()函数接收两个参数，一个是函数，一个是Iterable，
    map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
reduce()把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，
    reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
    reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
'''
# def f(x):
#     return x * x
# r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(list(r))
#
# # 把这个list所有数字转为字符串：
# print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

# # 把字符串变换成整数
# from functools import reduce
# CHAR_TO_INT = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
# def char2num(s):
#     return CHAR_TO_INT[s]
#
# def str2int(s):
#     def fn(x, y):
#         return x * 10 + y
#     return reduce(fn, map(char2num, s))
#
# def str2int2(s):
#     return reduce(lambda x, y: x * 10 + y, map(char2num, s))
#
# print(str2int("12345"))
# print(str2int2('0012345'))
