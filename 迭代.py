from collections import Iterable

list = ['a','b','c','d']
b = b'abcde'
for c in b:
    print(c)

dict = {"name":"zhangsan","gender":"male","age":30,"city":"beijing","mobile":"13401034709"}

for v in dict.values():
    print(v)

for k,v in dict.items():
    print(k,"=",v)

print(isinstance([1,2,3,4,5],Iterable))


print(isinstance('12456',Iterable))

print(isinstance(123,Iterable))

for i,k in enumerate(["aaaa",'bbbb','ccccc','ddddd','eeeeeee']):
    print(i,k)

for i,j,z in [('a','b','c'),(1,2,3),(3,4,4),('c','d','e')]:
    print(i,j,z)