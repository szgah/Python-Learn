import functools
#functools.partial函数的作用就是将一个函数包装起来，并将其中的一部分参数设置为默认参数固定下来，并返回一个新的函数。便于进行调用
def f1(x,y,*args):    
    return x+y+sum(args)
f2 = functools.partial(f1,1,2,3,4); 

print(f2(2,3))#返回15相当于调用函数f1(2,3,1,2,3,4)

max2 = functools.partial(max,10)
print(max2(3,4,5))#返回10 相当于调用max(10,3,4,5)

int2 = functools.partial(int,base=2)
print(int2("1000")) #返回8 相当于调用int("1000",base=2)