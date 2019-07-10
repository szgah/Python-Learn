#dict 字典的数据结构已键值对的形成存储数据，且要保证key值不可重复.
d = {"aaaa":1,"bbbbb":2,"cccc":3,"dddd":4}
d["eeeee"]=5 #添加一个新项目
d.pop("aaaa")
for k,v in d.items():
    print(k,"=",v)


s=set([1,2,3,4,5])
s.add((4,5))#添加一个项目
s.pop() #删除开头的项目
s.remove(2)#删除指定的项目.
for x in s:
    print(x)