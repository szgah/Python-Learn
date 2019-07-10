import os
#列表生成式是Python内构件list的生成方式
L=[]
#传统构件的方式。
for x in range(1,11):
    L.append(x*x)
print(L)

#使用列表生成式
cl=[x*x for x in range(1,11) if x%2==0]
print(cl)

c2=[x+"="+y for x,y in {"age":"30","name":"zhangsan","gender":"male"}.items()]
print(c2)

c3=[x+y for x in "abcd" for y in "efgh"]
print(c3)

d = [dir for dir in os.listdir("C:\\")]
print(d)

L = ['Hello', 'World', 'IBM', 'Apple']
print([x.lower() for x in L])

L1 = ['Hello', 'World', 18, 'Apple', None]
print([s.lower() for s in L1 if isinstance(s,str)])