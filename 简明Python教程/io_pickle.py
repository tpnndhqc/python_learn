import pickle

# 设置文件存储的路径
shoplistfile = 'shoplist.data'
shoplist = ['apple', 'mango', 'carrot']

# 需要通过  open  以写入（write）二进制（binary）模式打开文件，
# 然后调用  pickle  模块的  dump  函数将对象写入到文件。这一过程被称作封装（Pickling）
f = open(shoplistfile, 'wb')
pickle.dump(shoplist, f)
f.close()
# Destroy the shoplist variable
del shoplist

# Read back from the storage
f = open(shoplistfile, 'rb')
# 通过  pickle  模块的  load  函数接收返回的对象。这个过程被称作拆封（Unpickling）
storedlist = pickle.load(f)
print(storedlist)


