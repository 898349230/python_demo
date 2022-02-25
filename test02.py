#coding=utf-8

import os
import shutil

d = 'd:\\a\\'
for i in os.listdir(d):
    # print '----------',type(i)
    new_file = i.replace('~','new_file')
    old_full_file = d + '\\' + i
    new_full_file = d +  '\\' + new_file
    # print old_full_file.decode('GBK'),new_full_file.decode('GBK')
    shutil.move(old_full_file,new_full_file)
print ('DONE')

str = '我问'
file = open('d:\\a\\new_file111.txt','a')
file.write(str.decode('utf-8').encode('gbk'))
file.close()
# print 'done......'