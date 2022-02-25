#coding=utf-8

import sys
import re
from random import randint as aaa
if __name__ == '__main__':
    # for line in sys.stdin:
    #     line=1
    #     print line
    # print '############################3'

    aList=[1,3,4,5]
    # print aList
    del aList[2]
    # print aList

    # print '###########################  lambda 排序############################'

    data=[]
    data.append({'user':'s','pwd':'a','email':'aw'})
    data.append({'user':'a','pwd':'a','email':'ddd'})
    data.append({'user':'a','pwd':'b','email':'gg'})
    for d in data:
        print (d)
    print (data)
    data.sort(key=lambda x:(x['user'],x['pwd']),reverse=False)
    # print '##############排序后####################'
    for d in data:
        print (d)
    print (data)
    #from random import randint as aaa
    # print '随机数 ：', aaa(1,59)
    # print 'ad' in 'aaabf'
    # print 'ab' in 'abfd'

    print ('##############re模块######################')
    # 贪婪模式
    m = re.search('ab+','asdfdfeabbbbbbddfefe')
    print (m.group())
    # 非贪婪模式
    m = re.search('ab+?','asdfdfeabbbbbddfefe')
    print (m.group())
    pattern = re.compile("(asd)(dsa)")
    # pattern = re.compile("((asd)dsa)")   第一个分组：asddsa  第二个分组asd
    m=pattern.match("asddsagrg")
    # 正则分组
    print (m.group())
    print (m.group(0))
    print (m.group(1))  # 第一个正则分组
    print (m.group(2))  # 第二个正则分组
