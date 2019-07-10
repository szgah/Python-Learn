#python 中的迭代器

from collections import Iterable

print(isinstance([],Iterable))

print(isinstance((),Iterable))

print(isinstance("abc",Iterable))

g = (x for x in range(11)) #生成器
for i in g:
    print(i)

print(isinstance((x for x in range(11)),Iterable))


print(abs)