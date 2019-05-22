poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
use Python!
'''

# 打开模式可以是阅读模式（'r'），写入模式（'w'）和追加模式（'a'）及其他更多模式。
# 我们还可以选择是通过文本模式（'t'）还是二进制模式（'b'）来读取、写入或追加文本
f = open('D:\\poem.txt', 'w')   # 打开文件以编辑（'w'riting）
f.write(poem)   # 向文件中编写文本
f.close()   # 关闭文件

# 如果没有特别指定，将假定启用默认的阅读（'r'ead）模式
f = open('D:\\poem.txt')
while True:
    line = f.readline()
    # 零长度指示 EOF
    if len(line) == 0:
        break
    # 每行（`line`）的末尾 都已经有了换行符
    # 因为它是从一个文件中进行读取的
    print(line, end='')
# 关闭文件
f.close()
