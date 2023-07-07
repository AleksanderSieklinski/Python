#! /usr/bin/env python3
import keyword
import builtins
import math
#from math import sqrt
#from cmath import sqrt as csqrt
import sys
import cmath
#print(dir(''))
#print(dir(math))
#print(help(math.modf))
#print(dir(builtins))
#print('Hello',keyword.kwlist)
#print(type(''))
#print(type(""))
#a=7
#print(type(a))
#a=1.5
#print(type(a))
#a=1,5
#print(type(a))
#a,b=1,'2'
#print(type(a),type(b))
#a,*b=1,'2',3.,4,5
#print(type(a),type(b))
#print(1/2, 1//2)
#print(1./2, 1.//2)
#print(2**3, pow(2,3), math.pow(2,3))
#print(pow(2,3,4), pow(2,3,5))
#print(math.modf(1/3), math.modf(2.5))
#a=-1.7
#print(type(abs(a)), type(math.fabs(a)))
#a=-1
#print(type(abs(a)), type(math.fabs(a)))
#if len(sys.argv)!=5:
#    sys.exit()
#a=float(sys.argv[1])
#b=float(sys.argv[2])
#c=float(sys.argv[3])
#eps=float(sys.argv[4])
#if d>1e-6:
#    wynik=(-b-sqrt(d))/(2*a)
#    wynik1=(-b+sqrt(d))/(2*a)
#    print(f'Miejsca zerowe: {wynik}, {wynik1}')
#elif abs(d)<=1e-6:
#    wynik = -b/(2*a)
#    print(f'Miejsca zerowe: {wynik}')
#else:
#    wynik=(-b-csqrt(d))/(2*a)
#    wynik1=(-b+csqrt(d))/(2*a)
#    print(f'Miejsca zerowe: {wynik}, {wynik1}')
#if (d:=b*b-4*a*c)>eps:
#    wynik=(-b-math.sqrt(d))/(2*a)
#    wynik1=(-b+math.sqrt(d))/(2*a)
#    print(f'Miejsca zerowe: {wynik:.2f}, {wynik1:.2f}')
#elif math.fabs(d)<=eps:
#    wynik = -b/(2*a)
#    print(f'Miejsca zerowe: {wynik:.2f}')
#else:
#    wynik=(-b-cmath.sqrt(d))/(2*a)
#    wynik1=(-b+cmath.sqrt(d))/(2*a)
#    print(f'Miejsca zerowe: {wynik:.3f}, {wynik1:.3f}')
#print(d)
#k=()
#print(type(k))
#k=(2)
#print(type(k))
#k=(2,)
#print(type(k))
#k=(1,2.3,'3',(4,7),[3,4,5],)
#print(len(k))
#print(k[0],k[len(k)-1],k[-1])
#k[-1]='a'
#k[-1][1]='a'
#k[2][0]=6
#k[-2]=(2,9)
#k=[25,76,441,852,1230,57,32]
#print(k[:])
#print(k[2:-3])
#print(k[2:])
#print(k[:-3])
#print(k[::-3])
#s='slowo'
#print(s[::-1])
"""k=[1,2.3,'3',(4,7),[2,3,4],]
c=k[1]=[7,8,9]
print(c,k)
print(id(c),id(k))
c=k[:]
c[1]='7,8,9'
print(c,k)
print(id(c),id(k))
c[-1][1]='7,8,9'
print(c,k)
c=k.copy()
c[1]='7,8,9'
print(c,k)
print(id(c),id(k))
import copy
c=copy.copy(k)
c[1]='7,8,9'
print(c,k)
print(id(c),id(k))
c[-1][1]='7,8,9'
print(c,k)
c=copy.deepcopy(k)
c[1]='7,8,9'
print(c,k)
print(id(c),id(k))
c[-1][1]='7,8,9'
print(c,k)"""
