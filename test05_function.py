#coding=utf-8

def myFunc(num):
    return num+22
def convert(func,seq):
    return [func(num) for num in seq]
seqList=[1,2.3,-8.6e2,889]
# print convert(int,seqList)
print ("#######################")
# print convert(myFunc,seqList)

# '################################'
# tax默认值为u 0.05
def taxFun(cost,tax=0.05):
    return cost + cost * tax
# print taxFun(100)
# print taxFun(100,0.5)

# 不定长列表参数
print ('#############不定长列表参数###################')
def taxFun2(cost,tax=0.05,*restCost):
    for other in restCost:
        print ( "other arg : ",other)
        cost += other
    total = cost + cost*tax
    return total
print (taxFun2(100,0.05,200,300))

# 不定长字典参数
print ("#####不定长字典参数#####")
def taxFun3(cost,tax=0.06,**otherArgs):
    for key in otherArgs.keys():
        print ("otherArgs key : ",key," , otherArgs value :",otherArgs[key])
        cost += otherArgs[key]
    total = cost + cost*tax
    return total
testDic={"key01":100,"key02":200,"key03":300}
print (taxFun3(100,0.05,other=100,other2=200,other3=300))