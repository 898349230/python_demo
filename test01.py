class Fish:
    hungry = True
    def eat(self,food):
        if food is not None:
            self.hungry = False

class User:
    def __int__(self,name):
        self.name=name

    if __name__=="__main__":
        #
        aTuple = ('aa',12,90.9,'try')
        aList = [1,2,3,4,'ff']
        aList.append(456)
        # print aList
        # print '_________________'

        def test(self):
            return 1,2,3
        a,b,c = test()
        # print a

        aDict = {'host':'earth','name':'zhangsan'}
        # print aDict
        aDict['home'] = 666
        print (aDict)
        # print aDict.values()
        # print aDict.keys()
        # print aDict['host'],'fff'
        for i in aDict:
            print (i,aDict[i])
        # print '**********------------------'
        for i,key in enumerate(aDict):
            print (i, key, aDict[key])


        #
        # a = "112"
        # b = 66
        # g = 1
        # h = 2
        # (g,h) = (h,g)
        # d=e=f=22
        # pystr = 'Python'
        # print 'out : ' + pystr[-1]
        # print pystr * 2
        # print "%s is not equal %d"%(a,b)
        # print d,e,f
        # print g,h
        # print "'abc   def  ## '"
        # print '''
        #     abc  ##$$%
        #
        #         '''



