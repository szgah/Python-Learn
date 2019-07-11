#装饰器

#函数也是一个对象。可以赋值给一个变量。应此可以通过该变量来执行函数.
def now():
    print("hello")
f = now
f()

print(now.__name__) #__name__用于获取函数对象的名称. 输出now
print(f.__name__)  #输出 now

#装饰器: 代码运行期间动态添加功能的方式，称为装饰器.譬如我们在执行now方法时候，需要能够记录下日志.

#定义不带参数的装饰器
def log(func):
    def wrapper(*args,**kw):
        print("before %s() called" % (func.__name__))
        func(*args,**kw)
    return wrapper  

@log
def test():
    print("test")

test()


#定义一个带参数的装饰器
import functools
def log1(msg):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print("before %s===%s" % (msg,func.__name__))
            func()
        return wrapper
    return decorator

@log1("hello")
def demo2():
    print("demo")
demo2()