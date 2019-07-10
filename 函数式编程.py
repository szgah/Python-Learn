# 一个变量可以指向一个函数
f = abs
f(-10)
#函数名自身也是一个变量。abs()函数中abs就是一个指向获取绝对值的函数变量名称.
#我们可以通过 对函数名称进行重新的赋值，开修改函数名称的功能：
#abs=10.但一般不建议这样来处理.

#高阶函数: 可以接受一个函数作为参数的函数，我们就称为高阶函数.

def mysum(x,y,f):
    return f(x)+f(y)
print(mysum(-10,20,abs))

#map 函数: 接收两个参数，第一个参数是一个函数，第二个参数是一个Iterable的数据集合。
#map函数将序列的每个元素依次作用到第一个函数上面。并将结果作为一个新的Iterator返回.
def f1(s):
    return s*s

L = map(f1,list(range(11)))
print(set(L))

#Reduce函数:
from functools import reduce

def combile(x,y):    
    return x*10+y

L = reduce(combile,[1,2,3,4,5,6])#等价于combile(combile(combile(combile(combile(1,2),3),4),5),6)
print(L)

digital={"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
def char2num(x):
    return digital[x]
def str2num(str):   
    def f(x,y):
        return x*10+y
    return reduce(f,list(map(char2num,str)))

def d(x):
    return x*x

l = list(map(d,list(range(101))))
print(l)


total = reduce(lambda x,y: x*10+y,map(char2num,'123456'))
print(isinstance(total,int))
print("total=",total)


print(list(filter(lambda x: x%2==0,[0,1,1,2,3,4,5])))

print(list(sorted([1,2,3,4,-10,11,21])))