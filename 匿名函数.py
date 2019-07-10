#可以将一个匿名函数赋值给某个变量。然后通过该变量来调用函数.
#关键字lambda 表示一个匿名函数。后面的x，表示参数。冒号后面的是表达式，不用写return 语句.
f = lambda x: x-1
print(list(map(f,[1,2,3,4,5,6])))


#可以将一个匿名函数作为返回值.
def fun(x,y):
    return lambda :x*x+y*y


print(fun(3,4)())



print(lambda x: x*x)