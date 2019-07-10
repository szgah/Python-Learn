L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[0:3])#表示取从索引0到3.但是不包含3
print(L[0:])#表示从索引0 取到最后一个数
print(L[:4])#表示从索引0，取到4但是不包含4
print(L[:])#
print(L[-3:])
print(L[-3:-1])

L = list(range(101))
print(L[:10]) #取前10个数
print(L[-10:])#取后10个数
print(L[11:20])#取11到20个数
print(L[:10:2])#取前10个数，每两个取一个
print(L[::5])#取所有数，每5个取一个
#tuple也是一种list区别是tuple是不可变的。应此也可以使用切片操作。只是结果任然是一个tuple
print((0,1,2,3,4,5)[:3])
#字符串xxxxxx也可以看成是一个list只是每个元素是一个字符，应此也可用使用切片操作
print("beijing"[::2])
