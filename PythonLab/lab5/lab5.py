import random
import string
import sys

#1
def fun(strin):
    lis=''.join(['x' for x in strin if x != 'x' and x.isalpha()])
    dic1={i:str(random.randint(0,10)) for i in lis}
    diction=str.maketrans(''.join(i for i in dic1.keys()),''.join(str(i) for i in dic1.items()))
    lis.translate(diction)#prawie dziala
    print(lis)
    
strin=sys.argv[1]
fun(strin)
#2
def fun1(*b):
    lis=[]
    for i in b[0]:
        for j in b[1:len(b)]:
            if i not in j:
                break
        else:
            lis.append(i)
    print(lis)
    return lis
fun1([1,2,3],(1,3,5),[3,2])
#5
def find(szuk,min,max,srch='r',ile=[]):
    if(srch=='r'):
        los=random.randint(min,max)
    else:
        los=(max-min)/2+min
    ile.append(0)
    print(len(ile))
    print("wartosc:",los)
    if los==szuk:
        return
    find(szuk,los,max) if los<szuk else find(szuk,min,los)
find(13,10,20)
find(13,10,20,'grrr')
