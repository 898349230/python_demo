#coding=utf-8

# 继承 objcct
class AddrBookEntry(object):
    def __init__(self,name,phone):
        self.name = name
        self.phone = phone
        print ('Create inistance for : ',self.name)
    def updatePhone(self,new_phone):
        self.phone = new_phone
        print ("update phone for: ",self.phone)

# 创建实例
jhon = AddrBookEntry('jhon','18878787')
tim = AddrBookEntry('tim',898989)

# print jhon
# print jhon.name,jhon.phone
# print tim.phone

# print bool([])
# print bool(None)
# print bool([None])

# 取商
# print 5//2
# print 5.0//2
# print 3//2

# 取商和余数
# print divmod(15,6)

# 元组
a = ("one","two")
# print a[0]
b = "one",
# print b[0]
c = ("one",)
# print c[0]
d = "one","two"
# print d[0]
# 字符串
e = "one"
# print e[0]

def func(args=[]):
    args.append(1)
    # print args
# 默认值实在函数加载的时候指定一块内存地址所有有记忆功能
func()
func()
func()