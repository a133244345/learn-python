# -*- coding:utf-8 -*-
s1='姓名:路琦'
s2='学号:1403050112'
s3='班级:通风一班'

import math
v=2
R=8.31
T=300.15
V=0.1e-3
p1=v*R*T/V
print "p1=",p1

a=0.828
b=3.05*10**-2
c=1e-3
p2=v*R*T/(V-v*b)*c-(v**2)*a/(V**2)
print "p2=",p2