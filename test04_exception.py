#coding=utf-8

from test05_function import myFunc

def testFun():
    print ("testFun")
    print (myFunc(20))

testFun()

try:
    # 断言
    assert 1==0
except AssertionError as args:
    print ('has exception')

try:
    # 抛出异常
    raise ZeroDivisionError
except ZeroDivisionError as args:
    print ('gen exception')