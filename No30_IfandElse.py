#-*- coding:utf-8 -*-
people = 10
cars = 40
buses = 15

#ע�⣺������if ���� elif ����else��߶���һ��ð�ţ�Ȼ���������4���ո�һ��tab��
if cars > people:
	print "We should take the cars"
#��Ҫע����ǣ���python�� ���� else if������ elif!!!
elif cars < people:
	print "We should not take the cars"
else:
	print "We cannot decide"

if buses > cars:
	print "Thats too many buses"
elif buses < cars:
	print "Maybe we could take the buses"
else:
	print "We still cant decide"

if people > buses:
	print "Alright , let us take the buses."
else:
	print "Fine ,we stady at home then."