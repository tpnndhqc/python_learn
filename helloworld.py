# -*- coding: UTF-8 -*
#或者# coding=utf-8

#!/usr/bin/python
# Filename : helloworld.py	
#简明Python教程

#py1: 严格对齐,print前面不能有空格, Python 是区分大小写的
#print ('Hello World')

#py2: 连接多个字符串,保留全部空格
#print('The quick brown fox', 'jumps over  ', 'the lazy dog', "ces")

#py3: 没有单独的 long 类型。 int 类型可以指任何大小的整数
#print('1024 * 768 = ', 1024 * 768 )

#py4: print可以通过 end参数 指定其应以什么字符结尾，默认是换行‘\n’
# print('a', end='')
# print('b', end='输入')
# name = input()
# print('hello,', name)

#py5:双引号和单引号括起的字符串其工作机制完全相同
#name = input('please enter your name: ')
#print('hello,', name)

#py6: 比如\n表示换行，\t表示制表符，字符\本身也要转义，所以\\表示的字符就是\
# print( 1.23e9 )
# print('I\'m ok.')

#py7:用r''表示''内部的字符串默认不转义，指定一个原始（Raw） 字符
# print(r'\\\t\\')

#py8:用'''...'''的格式表示多行内容,输出中文需要文档修改为UTF-8格式。
# print('''这是一段多行字符串。
# This is the second line.
# "What's your name?," I asked.
# He said "Bond, James Bond."
# ''')

#py9: 布尔值及运算
#print (3>5)
#print (True and False)

#age = 15;
#if age >= 18:
    #print('adult')
#else:
    #print('teenager')

# 运算符与表达式
# +，-，*，**，/,//,%,<<,>>
# >,>=,<,<=,==,!=
# &,|,^,~     位运算(与，或，异或，取反)
# not,or,and  布尔(非，或，与)
#in, not in, is, is not 比较，包括成员资格测试和身份测试

#py10: 动态语言可以把任意数据类型赋值给变量
#a = 123 # a是整数
#print(a)
#a = 'ABC' # a变为字符串
#print(a)

#py11: 除/ ，地板除// ， 余数%
#print(10 // 3) 
#print(10 / 3)
#print(10 % 3)

#编码问题:
#1:用记事本编辑的时候，从文件读取的UTF-8字符被转换为Unicode字符到内存里，
#编辑完成后，保存的时候再把Unicode转换为UTF-8保存到文件：
#2:浏览网页的时候，服务器会把动态生成的Unicode内容转换为UTF-8再传输到浏览器：
#字符	ASCII		Unicode				UTF-8
#A		01000001	00000000 01000001	01000001
#中		x			01001110 00101101	11100100 10111000 10101101

#py12:获取默认编码
#import sys
#print(sys.getdefaultencoding())

#py13: ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
#print(ord('A'))
#print(ord('中'))   #'中' == 20013 == 0x4e2d
#print( chr(66))
#print( chr(25991)) #'文' == 25991 == 0x6587
#print( '\u4e2d\u6587') #中文
 
#py14: 对bytes类型的数据用带b前缀的单引号或双引号表示
		#以Unicode表示的str通过encode()方法可以编码为指定的bytes
		#从网络或磁盘上读取了字节流，读到的数据就是bytes。要把bytes变为str，就需要用decode()
#print(b'ABC')					#b'ABC'		
#print('ABC'.encode('ascii'))	#b'ABC'

#print( '中文'.encode('utf-8'))	#b'\xe4\xb8\xad\xe6\x96\x87'
#print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))	#中文

#b=u'好'
#print(type(b),len(b),b)		#<class 'str'> 1 好
#c = b.encode('utf-8')
#print(type(c),len(c),c)		#<class 'bytes'> 3 b'\xe5\xa5\xbd'
#d = c.decode('utf-8')
#print(type(d),len(d),d)		#<class 'str'> 1 好


#py15:对于str,len()函数计算的是str的字符数, 对于bytes，len()函数计算字节数：
#s = 'id\u003d215903184\u0026index\u003d0\u0026st\u003d52\u0026sid\u003d95000\u0026i'
#print(type(s),len(s), s)	#<class 'str'>  id=215903184&index=0&st=52&sid=95000&i
#e= s.encode('ascii')
#print(type(e),len(e), e)	#<class 'bytes'> b'id=215903184&index=0&st=52&sid=95000&i'

#s = u'id\u003d215903184\u0026index\u003d0\u0026st\u003d52\u0026sid\u003d95000\u0026i'
#print(type(s),len(s), s)	#<class 'str'>  id=215903184&index=0&st=52&sid=95000&i
#f=s.encode('utf-8')
#print(type(f),len(f), f)	#<class 'bytes'> b'id=215903184&index=0&st=52&sid=95000&i'
#g = f.decode('utf-8')
#print(type(g),len(g), g)	#<class 'str'>  id=215903184&index=0&st=52&sid=95000&i


#导入某个模块库  import chardet
#for i in ['abc123','中国']:
    #print (i,chardet.detect(i))


#格式化方法, {0}这种数字只是一个可选选项，但是可以帮助识别第几个参数。
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



