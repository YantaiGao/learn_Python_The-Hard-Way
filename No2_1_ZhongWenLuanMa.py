# -*- coding:utf -8-*-

print "高延太".decode('utf-8').encode('gbk')


import sys

type = sys.getfilesystemencoding()

print "高延泰".decode('utf-8').encode(type)