try:
    f = open("E:\\公司服务器地址.txt",'r')
    print(f.read())
finally:
    if f:
        f.close()