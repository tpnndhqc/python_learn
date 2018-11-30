# -*- coding: UTF-8 -*
#或者# coding=utf-8

#!/usr/bin/python
# Filename : helloworld.py	
#简明Python教程

# # # # # # # # # #     基本问题    # # # # # # # # # #
# # py1: 严格对齐,print前面不能有空格, Python 是区分大小写的
# print ('Hello World')

# # py2: 连接多个字符串,保留全部空格
# print('The quick brown fox', 'jumps over  ', 'the lazy dog', "ces")

# # py3: 没有单独的 long 类型。 int 类型可以指任何大小的整数
# print('1024 * 768 = ', 1024 * 768 )

# # py4: print可以通过 end参数 指定其应以什么字符结尾，默认是换行‘\n’
# print('a', end='')
# print('b', end='输入')
# name = input()
# print('hello,', name)

# # py5:双引号和单引号括起的字符串其工作机制完全相同
# name = input('please enter your name: ')
# print('hello,', name)
#
# # py6: 比如\n表示换行，\t表示制表符，字符\本身也要转义，所以\\表示的字符就是\
# print( 1.23e9 )
# print('I\'m ok.')
#
# # py7:用r''表示''内部的字符串默认不转义，指定一个原始（Raw） 字符
# print(r'\\\t\\')

# # py8:用'''...'''的格式表示多行内容,输出中文需要文档修改为UTF-8格式。
# print('''这是一段多行字符串。
# This is the second line.
# "What's your name?," I asked.
# He said "Bond, James Bond."
# ''')

# # py9: 布尔值及运算
# print (3>5)
# print (True and False)
#
# age = 15;
# if age >= 18:
#     print('adult')
# else:
#     print('teenager')

# # 运算符与表达式
# +，-，*，**，/,//,%,<<,>>
# >,>=,<,<=,==,!=
# &,|,^,~     位运算(与，或，异或，取反)
# not,or,and  布尔(非，或，与)
# in, not in, is, is not 比较，包括成员资格测试和身份测试

# # py10: 动态语言可以把任意数据类型赋值给变量
# a = 123 # a是整数
# print(a)
# a = 'ABC' # a变为字符串
# print(a)

# # py11: 除/ ，地板除// ， 余数%
# print(10 // 3)
# print(10 / 3)
# print(10 % 3)

# # py12:格式化方法, {0}这种数字只是一个可选选项，但是可以帮助识别第几个参数。
# age = 20
# name = 'Swaroop'
# print('{0} was {1} years old when he wrote this book'.format(name, age))
# # 基于关键词。输出 'Swaroop wrote A Byte of Python'
# print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))
# # 对于浮点数保留小数点(.)后三位，输出: 0.333
# print('{0:.3f}'.format(1.0/3))
# # 使用下划线填充文本，并保持文字处于中间位置
# # 使用 (^) 定义 '___hello___'字符串长度为 11。输出: ___hello___
# print('{0:_^11}'.format('hello'))


# # # # # # # # # #     编码相关问题    # # # # # # # # # #

# 1:用记事本编辑的时候，从文件读取的UTF-8字符被转换为Unicode字符到内存里，
# 编辑完成后，保存的时候再把Unicode转换为UTF-8保存到文件：
# 2:浏览网页的时候，服务器会把动态生成的Unicode内容转换为UTF-8再传输到浏览器：
# 字符	ASCII		Unicode				UTF-8
# A		01000001	00000000 01000001	01000001
# 中		x			01001110 00101101	11100100 10111000 10101101

# # py:获取默认编码
# import sys
# print(sys.getdefaultencoding())

# # py13: ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
# print(ord('A'))
# print(ord('中'))   #'中' == 20013 == 0x4e2d
# print( chr(66))
# print( chr(25991)) #'文' == 25991 == 0x6587
# print( '\u4e2d\u6587') #中文

# # py: 对bytes类型的数据用带b前缀的单引号或双引号表示
# # 		以Unicode表示的str通过encode()方法可以编码为指定的bytes
# # 		从网络或磁盘上读取了字节流，读到的数据就是bytes。要把bytes变为str，就需要用decode()
# print(b'ABC')					#b'ABC'
# print('ABC'.encode('ascii'))	#b'ABC'
#
# print( '中文'.encode('utf-8'))	#b'\xe4\xb8\xad\xe6\x96\x87'
# print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))	#中文
#
# b=u'好'
# print(type(b),len(b),b)		#<class 'str'> 1 好
# c = b.encode('utf-8')
# print(type(c),len(c),c)		#<class 'bytes'> 3 b'\xe5\xa5\xbd'
# d = c.decode('utf-8')
# print(type(d),len(d),d)		#<class 'str'> 1 好

# # py:对于str,len()函数计算的是str的字符数, 对于bytes，len()函数计算字节数：
# s = 'id\u003d215903184\u0026index\u003d0\u0026st\u003d52\u0026sid\u003d95000\u0026i'
# print(type(s),len(s), s)	#<class 'str'>  id=215903184&index=0&st=52&sid=95000&i
# e= s.encode('ascii')
# print(type(e),len(e), e)	#<class 'bytes'> b'id=215903184&index=0&st=52&sid=95000&i'
#
# s = u'id\u003d215903184\u0026index\u003d0\u0026st\u003d52\u0026sid\u003d95000\u0026i'
# print(type(s),len(s), s)	#<class 'str'>  id=215903184&index=0&st=52&sid=95000&i
# f=s.encode('utf-8')
# print(type(f),len(f), f)	#<class 'bytes'> b'id=215903184&index=0&st=52&sid=95000&i'
# g = f.decode('utf-8')
# print(type(g),len(g), g)	#<class 'str'>  id=215903184&index=0&st=52&sid=95000&i


# # # # # # # # # #     控制流相关问题    # # # # # # # # # #

# # py:for 循环
# for i in range(1, 5):
# 	print(i)
# else:
# 	print('The for loop is over')

# # py:while 语句，while可以跟else，它与if-else的逻辑等同，条件为False时开始执行。
# number = 23
# running = True
# while running:
# 	guess = int(input('Enter an integer : '))
# 	if guess == number:
# 		print('Congratulations, you guessed it.')
# 		running = False
# 	elif guess < number:
# 		print('No, it is a little higher than that.')
# 	else:
# 		print('No, it is a little lower than that.')
# else:
# 		print('The while loop is over.')
# # 在这里你可以做你想做的任何事
# print('Done')


# # # # # # # # # #     函数相关问题    # # # # # # # # # #

# # py:函数调用
# def say_hello():
# 	print('hello world')
#
# say_hello() # 调用函数

# # py:global 语句
# x = 50
# def func():
# 	global x
# 	print('x is', x)
# 	x = 2
# 	print('Changed global x to', x)
#
# func()
# print('Value of x is', x)
#
# global 语句用以声明 x 是一个全局变量，
# 当我们在函数中为 x 进行赋值时，这一改动将影响到我们在主代码块中使用的 x 的值。
# 否则只是改变了函数里面的局部变量 x, 它的作用域为定义点到自身代码块结束，主代码块的 x 不会被改变。

# # py:函数的默认参数值，只有位于参数列表末尾的参数才能被赋予默认参数值
# def say(message, times=1):
# 	print(message * times)
# say('Hello')
# say('World', 5)

# # py:函数使用关键字参数
# def func(a, b=5, c=10):
# 	print('a is', a, 'and b is', b, 'and c is', c)
# func(c=50, a=100)
# # 输出:a is 100 and b is 5 and c is 50

# # py:可变参数
# def total(a=5, *numbers, **phonebook):
#     print('a', a)
#     #遍历元组中的所有项目
#     for single_item in numbers:
#         print('single_item', single_item)
#     #遍历字典中的所有项目
#     for first_part, second_part in phonebook.items():
#         print(first_part,second_part)
# print(total(10,1,46,48,John='hello',Inge=1990))
# # 当声明诸如 *param 的星号参数时，从此处开始直到结束的所有位置参数[1,46,48]都将被收集并汇集成一个元组（Tuple）。
# # 当声明诸如 **param 的双星号参数时，从此处开始直至结束的所有关键字参数[John='hello',Inge=1990]都将被收集并汇集成字典（Dictionary）。

# # py: Python 中的 pass 语句用于指示一个没有内容的语句块；如果函数没有return语句，则结尾默认添加return None。
# def some_function():
#     pass

# # py: 文档字符串 DocStrings，使用''' something'''格式
# # 文档字符串所约定，其中第一行以某一大写字母开始，以句号结束。第二行为空行，后跟的第三行开始是任何详细的解释说明。
# def print_max(x, y):
#     '''Prints the maximum of two numbers.打印两个数值中的最大数。
#     The two values must be integers.这两个数都应该是整数'''
#     x = int(x)
#     y = int(y)
#     if x > y:
#         print(x, 'is maximum')
#     else:
#         print(y, 'is maximum')
# print_max(3, 5)
#
# print(print_max.__doc__)
# help(print_max)


# # # # # # # # # #     模块相关问题    # # # # # # # # # #

# # py:导入某个模块库  import chardet
# for i in ['abc123','中国']:
#     print (i,chardet.detect(i))

# # py:sys 模块包含了与 Python 解释器及其环境相关的功能，也就是所谓的系统功能（system）。
# import sys
# import os;
# print('The command line arguments are:')
# for i in sys.argv:
#     print(i)
# print(os.getcwd())
# print('\n\nThe PYTHONPATH is', sys.path, '\n')

#类似于C++的命名空间  from sys import argv，不建议使用 #从sys中导出argv
# from helloworld import say_hi, __version__  #导出say_hi及__version__
# from helloworld import *   #导出helloworld中的全部函数及变量，不包括双下划线开头的变量如:__version__

# # py:编写你自己的模块
#引入helloworld.py文件，每一个 Python 程序同时也是一个模块，可以直接在file2中引入file1进来使用它的函数及变量。
# #file1: F:\Python\Project\helloworld.py
# def say_hi():
#     if __name__ == '__main__':
#         print('run by itself')
#     else:
#         print('run by another module')
# __version__ = '0.1'
#
# #file2: F:\Python\Project\mymodule_demo.py
# import helloworld
# helloworld.say_hi()
# print('file2:', __name__)
# print('file1:', helloworld.__name__, helloworld.__version__)

# # py:dir函数导出返回由对象所定义的名称列表。 如果这一对象是一个模块，则该列表会包括函数内所定义的函数、类与变量。
# #如果参数是模块名称，函数将返回这一指定模块的名称列表
# #如果没有提供参数，函数将返回当前模块的名称列表。
# import string
# a = 5
# print(dir())
# del a
# print(dir())
# print(dir(string))

# 包是指一个包含模块与一个特殊的 __init__.py 文件的文件夹，后者向 Python 表明这一文件夹是特别的，因为其包含了 Python 模块。
# # 创建一个名为“world”的包，其中还包含着“asia”及其它子包，同时这些子包都包含了诸如“india”等模块。
# <some folder present in the sys.path>/
# - world/
# 	- __init__.py
# 	- asia/
# 		- __init__.py
# 		- india/


# # # # # # # # # #     数据结构相关问题    # # # # # # # # # #
# Python 中有四种内置的数据结构
# ——列表（List）、元组（Tuple）、字典（Dictionary）和集合（Set）
# 列表是可变的，元组是不可变的。

# 列表：常用函数：sort(), append('*')
# shoplist = ['apple', 'mango', 'carrot', 'banana']
# for item in shoplist:
#     print(item, end=' ')

# 元组：zoo = ('python', 'elephant', 'penguin'
    # 只拥有一个元素的元组singleton = (2, )

# 字典：常用函数：items()
# Address = {
#     'Swaroop': 'swaroop@swaroopch.com',
#     'Larry': 'larry@wall.org',
#     'Matsumoto': 'matz@ruby-lang.org',
#     'Spammer': 'spammer@hotmail.com'
# }
# print("Swaroop's address is", Address['Swaroop'])
# for name, address in Address.items():
#     print('Contact {} at {}'.format(name, address))

# 序列：序列的主要功能是资格测试（也就是in与not in表达式）和索引操作，它们能够允许我们直接获取序列中的特定项目。
# # 要注意的是切片操作会在开始处返回 start，并在 end 前面的位置结束工作。也就是说，序列切片将包括起始位置，但不包括结束位置。
# # 比如shoplist[1:3]表示从下标1开始到3结束，但是不包括下标3。结果为['mango', 'carrot']。
# # shoplist[-1]  指的是序列的最后一个项目。
# shoplist = ['apple', 'mango', 'carrot', 'banana']
# name = 'swaroop'
# # 索引或“下标（Subscription）”操作符 #
# print('Item 0 is', shoplist[0])
# # Slicing on a list #
# print('Item 1 to -1 is', shoplist[1:-1])
# # 从某一字符串中切片 #
# print('characters 2 to end is', name[2:])
# # 可以在切片操作中提供第三个参数，这一参数将被视为切片的步长（Step）
# print(shoplist[::1])
# print(shoplist[::2])
# print(shoplist[::-1])

# 集合：集合（Set）是简单对象的无序集合（Collection）。当集合中的项目存在与否比起次序或其出现次数更加重要时，我们就会使用集合。
# bri = set(['brazil', 'russia', 'india'])
# print('india' in bri) #True
# bric = bri.copy()
# bric.add('china')
# print(bric)         #{'russia', 'india', 'china', 'brazil'}
# print(bric.issuperset(bri))   #True
# print(bri & bric)             #{'russia', 'india', 'brazil'}

# py:必须使用切片操作来制作复杂对象的副本。如果你仅仅是将一个变量名赋予给另一个名称，那么它们类似与引用，都指向同一个对象。
# print('Simple Assignment')
# shoplist = ['apple', 'mango', 'carrot', 'banana']
# # mylist 只是指向同一对象的另一种名称
# mylist = shoplist
# # mylistcopy 通过生成一份完整的切片制作一份列表的副本
# mylistcopy = shoplist[:]
# # 我购买了第一项项目，所以我将其从列表中删除
# del shoplist[0]
# print('shoplist is', shoplist)
# print('mylist is', mylist)
# print('mylistcopy is', mylistcopy)

# py:字符串函数
# # startwith  方法用于查找字符串是否以给定的字符串内容开头。
# # find  方法用于定位字符串中给定的子字符串的位置
# # in   运算符用以检查给定的字符串是否是查询的字符串中的一部分。
# # str  类同样还拥有一个简洁的方法用以联结序列中的项目，其中字符串将会作为每一项目之间的分隔符，并以此生成并返回一串更大的字符串。
# name = 'Swaroop'
# if name.startswith('Swa'):
#     print('Yes, the string starts with "Swa"')
# if 'a' in name:
#     print('Yes, it contains the string "a"')
# if name.find('war') != -1:
#     print('Yes, it contains the string "war"')
# delimiter = '_*test*_'
# mylist = ['Brazil', 'Russia', 'India', 'China']
# print(delimiter.join(mylist))

# 一个简单的示例程序
# import os
# import time
# # 1. 需要备份的文件与目录将被指定在一个列表中。
# # 例如在 Windows 下：
# source = ['"D:\\1样本\\test"']
# # 又例如在 Mac OS X 与 Linux 下：
# # source = ['/Users/swa/notes']
# # 在这里要注意到我们必须在字符串中使用双引号,用以括起其中包含空格的名称。
# # 2. 备份文件必须存储在一个主备份目录中
# # 例如在 Windows 下：
# target_dir = 'D:\\新建文件夹 (2)\\Backup'
# # 又例如在 Mac OS X 和 Linux 下：
# # target_dir = '/Users/swa/backup'
# # 要记得将这里的目录地址修改你将使用的路径,如果目标目录不存在则创建目录
# if not os.path.exists(target_dir):
#     os.mkdir(target_dir) # 创建目录
# # 3. 备份文件将打包压缩成 zip 文件。
# # 4. 将当前日期作为主备份目录下的子目录名称
# today = target_dir + os.sep + time.strftime('%Y%m%d')
# # 将当前时间作为 zip 文件的文件名
# now = time.strftime('%H%M%S')
# # zip 文件名称格式
# target = today + os.sep + now + '.zip'
# # 如果子目录尚不存在则创建一个
# if not os.path.exists(today):
#     os.mkdir(today)
# print('Successfully created directory', today)
# # 5. 我们使用 zip 命令将文件打包成 zip 格式
# zip_command = 'zip -r {0} {1}'.format(target,' '.join(source))
# # 运行备份
# print('Zip command is:')
# print(zip_command)
# print('Running:')
# if os.system(zip_command) == 0:
#     print('Successful backup to', target)
# else:
#     print('Backup FAILED')


# # # # # # # # # #     面向对象编程    # # # # # # # # # #
# # py: self 关键字
# Python 中的  self  相当于 C++ 中的指针以及 Java 与 C# 中的  this  指针。
# 假设你有一个  MyClass  的类，这个类下有一个实例  myobject  。
# 当你调用一个这个对象的方法，如  myobject.method(arg1, arg2)  时，
# Python 将会自动将其转换成  MyClass.method(myobject, arg1, arg2)  ——这就是  self  的全部特殊之处所在。

# # py: 类 和 方法, __init__ 初始化方法
# class Person:
#     def __init__(self, name):
#         self.name = name
#     def say_hi(self):
#         print('Hello, my name is', self.name)
# p = Person('sping')
# p.say_hi()
# print(p)

# #  py: 类变量与对象变量
# 参照 F:\工作\Python\Project\Robot.py
# 类变量（Class Variable）是共享的（Shared）——它们可以被属于该类的所有实例访问。
# 该类变量只拥有一个副本，当任何一个对象对类变量作出改变时，发生的变动将在其它所有实例中都会得到体现。
# 对象变量（Object variable）由类的每一个独立的对象或实例所拥有。
# 在这种情况下，每个对象都拥有属于它自己的字段的副本，也就是说，它们不会被共享，也不会以任何方式与其它不同实例中的相同名称的字段产生关联

# #  py: 继承
# 参照 F:\工作\Python\Project\oop_subclass.py


# # # # # # # # # #     输入与输出    # # # # # # # # # #
# # py: 分别通过  input()  函数与  print()  函数来实现 输入与输出

# # py: 文件读写
# 创建 file  类的对象，并使用它的  read 、readline 、write、close 方法来打开或使用文件，并对它们进行读取或写入。
# 参考 F:\工作\Python\Project\io_using_file.py

# # py: 持久化存储对象 Pickle
# 需要通过  open  以写入（write）二进制（binary）模式打开文件，
# 调用  pickle  模块的  dump  函数将对象写入到文件。这一过程被称作封装（Pickling）
# 通过  pickle  模块的  load  函数接收返回的对象。这个过程被称作拆封（Unpickling）

# # py: Unicode
# 如果我们需要使用 unicode 类型，它全都以字母 u 开头
# # encoding=utf-8
# import io
# f = io.open("abc.txt", "wt", encoding="utf-8")
# f.write(u"Imagin 中文的 language here")
# f.close()
# text = io.open("abc.txt", encoding="utf-8").read()
# print(text)

# # # # # # # # # #     异常    # # # # # # # # # #
# # py: 通过  raise  语句来抛出异常
# # encoding=UTF-8
# class ShortInputException(Exception):
#     '''一个由用户定义的异常类'''
#     def __init__(self, length, atleast):
#         Exception.__init__(self)
#         self.length = length
#         self.atleast = atleast
# try:
#     text = input('Enter something --> ')
#     if len(text) < 3:
#         raise ShortInputException(len(text), 3)
#     # 其他工作能在此处继续正常运行
# except EOFError:
#     print('Why did you do an EOF on me?')
# except ShortInputException as ex:
#     print(('ShortInputException: The input was ' +
#     '{0} long, expected at least {1}')
#     .format(ex.length, ex.atleast))
# else:
#     print('No exception was raised.')


# 确保对象被正确关闭，无论是否会发生异常？这可以通过  finally  块来完成
# # 方式一：Try ... Finally  在try块中获取资源，然后在finally块中释放资源是一种常见的模式
# import sys
# import time
# f = None
# try:
#     f = open('poem.txt')
#     while True:
#         line = f.readline()
#         if len(line) == 0:
#             break
#         print(line, end='')
#         sys.stdout.flush()
#         # time.sleep(1)
# except IOError:
#     print("Could not find file poem.txt")
# except KeyboardInterrupt:
#     print("!! You cancelled the reading from the file.")
# finally:
#     if f:
#         f.close()
# print("(Cleaning up: Closed the file)")
#
# # 方式二： with  语句
# with open("poem.txt") as f:
#     for line in f:
#         print(line, end='')
#

# # # # # # # # # #     标准库    # # # # # # # # # #
# # 探索标准库的最好方法是阅读由 Doug Hellmann 撰写的优秀的Python Module of theWeek 系列
# # os  模块用以和操作系统交互。 主驱动器：os.getenv('HOMEDRIVE'), 主文件夹：os.getenv('HOMEPATH')
# # platform  模块用以获取平台 操作系统 的信息，
# # logging  模块用来记录（Log）信息
# import os
# import platform
# import logging
#
# #输出正在使用的操作系统版本如： Windows-7-6.1.7601-SP1
# print(platform.platform())
# if platform.platform().startswith('Windows'):
#     logging_file = os.path.join(os.getenv('HOMEDRIVE'), os.getenv('HOMEPATH'), 'test.log')
# else:
#     logging_file = os.path.join(os.getenv('HOME'), 'test.log')
# print("Logging to", logging_file)
#
# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%(asctime)s : %(levelname)s : %(message)s',
#     filename=logging_file,
#     filemode='w',
# )
# logging.debug("Start of the program")
# logging.info("Doing something")
# logging.warning("Dying now")

# # # # # # # # # #     其他    # # # # # # # # # #
# # py: 使用元组返回多个不同的值
# def get_error_details():
#     return (2, 'details')
# errnum, errstr = get_error_details()
# print(errnum)
# print(errstr)

# # py: Python 中交换两个变量的最快方法
# a = 5; b = 8
# a, b = b, a
# print(a, b)

# # py: 特殊方法
# __init__(self, ...)
# 这一方法在新创建的对象被返回准备使用时被调用。
# __del__(self)
# 这一方法在对象被删除之前调用（它的使用时机不可预测，所以避免使用它）
# __str__(self)
# 当我们使用  print  函数时，或  str()  被使用时就会被调用。
# __lt__(self, other)
# 当小于运算符（<）被使用时被调用。类似地，使用其它所有运算符（+、> 等等）
# 时都会有特殊方法被调用。
# __getitem__(self, key)
# 使用  x[key]  索引操作时会被调用。
# __len__(self)
# 当针对序列对象使用内置  len()  函数时会被调用

# # py: Lambda 表格
# lambda  语句可以创建一个新的函数对象。
# 从本质上说， lambda  需要一个参数，后跟一个表达式作为函数体，这一表达式执行的值将作为这个新函数的返回值
# points = [  {'x': 2, 'y': 3},
#             {'x': 4, 'y': 1} ]
# points.sort(key=lambda i: i['y'])
# print(points)

# # py: 列表推导 #输出 [6, 8]
# listone = [2, 3, 4]
# listtwo = [2*i for i in listone if i > 2]
# print(listtwo)

# # py: 在函数中接收元组与字典
# 因为我们在 args 变量前添加了一个 * 前缀，函数的所有其它的额外参数都将传递到 args 中，并作为一个元组予以储存。
# 如果采用的是 ** 前缀，则额外的参数将被视为字典的键值—值配对。
# def powersum(power, *args):
#     '''Return the sum of each argument raised to the specified power.'''
#     total = 0
#     for i in args:
#         total += pow(i, power)
#     return total
# print(powersum(2, 3, 4))
# print(powersum(2, 10))

# # py: 装饰器
# # 装饰器（Decorators）是应用包装函数的快捷方式。这有助于将某一功能与一些代码一遍又一遍地“包装”。
# from time import sleep
# from functools import wraps
# import logging
# logging.basicConfig()
# log = logging.getLogger("retry")
#
# def retry(f):
#     @wraps(f)
#     def wrapped_f(*args, **kwargs):
#         MAX_ATTEMPTS = 5
#         for attempt in range(1, MAX_ATTEMPTS + 1):
#             try:
#                 return f(*args, **kwargs)
#             except:
#                 log.exception("Attempt %s/%s failed : %s",
#                               attempt,MAX_ATTEMPTS, (args, kwargs))
#                 sleep(10 * attempt)
#         log.critical("All %s attempts failed : %s",
#                      MAX_ATTEMPTS,(args, kwargs))
#         return wrapped_f
# counter = 0
#
# @retry
# def save_to_database(arg):
#     print("Write to a database or make a network call or etc.")
#     print("This will be automatically retried if exception is thrown.")
#     global counter
#     counter += 1
#     # 这将在第一次调用时抛出异常
#     # 在第二次运行时将正常工作（也就是重试）
#     if counter < 2:
#         raise ValueError(arg)
#     if __name__ == '__main__':
#         save_to_database("Some bad value")
