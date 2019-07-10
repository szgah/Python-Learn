import math
#返回的是一个tuple
def move(x,y,step,angle=0):
    nx = x+step*math.cos(angle)
    ny = y+step*math.cos(angle)
    return nx,ny

mx,my = move(100,100,60,math.pi/6)
print("mx=",mx,"&my=",my)

# 函数定义的总结:
#  1 函数定义的基本格式
#     def 函数名称 (参数列表):
#             函数体
#  2 isinstance(x,(type1,type2))可用于对参数类型做判断
#  3 函数执行完毕也没有return 的 返回的none
#  4  函数可以返回多个参数，其实返回的是tuple对象.
