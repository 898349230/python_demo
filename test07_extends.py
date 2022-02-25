#coding=utf-8

print ('#####################深度优先##########################')
# 没有object深度优先
class P1:
    def a(self):
        print ('P1 a...')
class P2:
    def a(self):
        print ('P2 a...')
    def b(self):
        print ('P2 b...')
class C1(P1,P2):
   pass

class C2(P1,P2):
    def b(self):
        print ('C2 b...')

class GC(C1,C2):
    pass
gc = GC()
gc.a()
gc.b()

print ('#################广度优先#########################')
# 有object广度优先
class P1(object):
    def a(self):
        print ('P1 a...')

class P2(object):
    def a(self):
        print ('P2 a...')
    def b(self):
        print ('P2 b...')

class C1(P1,P2):
    pass

class C2(P1,P2):
    def b(self):
        print ('C2 b...')

class GC(C1,C2):
    pass
gc = GC()
gc.a()
gc.b()