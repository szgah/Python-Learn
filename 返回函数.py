
def count():
    fs = []
    def f(i):
        def g():
            return i*i
        return g
    for j in range(1,4):
        fs.append(f(j))
    return fs

    
f1, f2, f3 = count()

print(f1())
print(f2())
print(f3())