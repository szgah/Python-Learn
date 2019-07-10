#函数的参数
#1 默认参数,必选参数在前,默认参数必须放在后面
def power(x,n=2):
    s = 1
    while n>0:
        n = n-1
        s = s*x
    return s

print(power(5,3))

def enroll(name,gender,age=6,city='beijing'):
     print("name=",name)
     print("gender=",gender)
     print("age=",age)
     print("city=",city)

enroll("施宗刚",'male')
enroll("施宗刚",'male',30)
enroll("施宗刚",'male',city="安庆")

#默认参数一般使用不变对象
def add_end(L=None):
    if L is None:
        L = []
    L.append("End")
    return L

print(add_end())
print(add_end())


#可变参数，参数的个数可以不固定.
def sum(*numbs):
    sum = 0
    for n in numbs:
        sum+=(n*n)
    return sum

sum = sum(*(1,2,3,4,5))
print("sum=",sum)

#关键字参数
def person(name,gender,**others):
    if 'city' in others:
        print("have city argument")
    if 'age' in others:
        print("have age argument")
    print("name=",name)
    print("gender=",gender)
    print("others=",others)


person("张三","男",city="sssss",age="30岁")

extrac = {"city":"北京","age":"30岁"}

person("张三","男")
person("张三","男",**extrac)

#命名关键字参数
def person1(name,gender,*,city,age):
    print("name=",name)
    print("gender=",gender)
    print("city=",city)
    print("age=",age)

person1("szg","male",city="aaaa",age="ssdfdsf")


#python 中函数的参数有必选参数，默认参数，可变参数，关键字参数，命名关键字参数 五种。
#这五种参数可以进行组合。但是组合的顺序必选为必选参数，默认参数，可变参数，命名关键字参数，关键字参数

def f1(a,b,c=0,*d,e,**f):
     print(a)
     print(b)
     print(c)
     print(d)
     print(e)
     print(f)

def f2(a,b,d=4,*,e,**f):
    pass

args=(1,2,3,4,5,6,7)
dict = {"e":"eeeeee","age":30,"gender":"male","city":"beijing","country":"china"}

f1(*args,**dict)


def fac(n):
    if n==1:
        return n
    return n*fac(n-1)

print(fac(200))


