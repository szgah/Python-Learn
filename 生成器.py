L=[x for x in range(1,11)]
print(L)
#1 通过列表生成式构件生成器
# g = (x for x in range(1,11))
# for x in g:
#     print(x)
#通过函数来构件生成器
def fib(max):
    n,a,b = 0,0,1
    while n<max:
        yield b
        a,b = b,a+b
        n=n+1        
    return 'done'

print(fib(6))
g = fib(6)
for x in g:
    print(x)

while True:
    try:
        print(next(g))
    except StopIteration as s:
        print("generator reutun value:",s.value)
        break

def odd():
    print("step 1")
    yield
    print("step 2")
    yield
    print("step 3")
    yield

o = odd()
next(o)
print("............................")
next(o)
print("............................")
next(o)
print("............................")

