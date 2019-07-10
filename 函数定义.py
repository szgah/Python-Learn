def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('incorrecct type')
    if x>0:
        return x
    else:
        return -x

arrar = [2,3,1,4,6,9,5]
arrar.sort()
print(arrar)

my_abs('x')