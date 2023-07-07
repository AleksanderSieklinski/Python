#zad1 Proszę napisać program testujący alternatywne sposoby budowania zestawu wartości: pętla for, lista składana, funkcja map i wyrażenie generatorowe (składnia taka jak listy składanej tylko w miejsce nawiasów kwadratowych należy wstawić okrągłe; o generatorach będziemy mówić na kolejnych zajęciach). Dla każdego ze sposobów proszę utworzyć osobną funkcję
print("zad1")
import time
import sys
import functools
import math
import random

powt=1000
N=10000
def tester(testFunction):
    start=time.time_ns()
    for i in range(powt):
        testFunction(N)
    return time.time_ns()-start

def forStatement(N):
    L=[]
    for i in range(N):
        L.append(i)

def listComprehension(N):
    L=[i for i in range(N)]

def mapFunction(N):
    L=list(map(lambda x:x, range(N)))

def generatorExpression(N):
    L=list((i for i in range(N)))
print(sys.version)
test=(forStatement, listComprehension, mapFunction, generatorExpression)
for testFunction in test:
    print(testFunction.__name__.ljust(20), '=>', tester(testFunction))
#zad2 Proszę wyznaczyć wartość liczby pi metodą Monte-Carlo korzystając z funkcji filter
print("zad2")
x=2
y=2
ile=10000
pkt=math.hypot(x/2,y/2)
l=((random.uniform(-x/2,x/2),random.uniform(-y/2,y/2)) for i in range(ile))
filt=filter(lambda xy: 1>math.hypot(*xy),l)
wart_pi=x**2*len(list(filt))/ile
print(wart_pi)
#zad3 Proszę napisać funkcję przyjmującą dwa parametry - lista x-ów i y-ów. Korzystając z funkcji wbudowanych sum i map proszę obliczyć (i zwrócić z funkcji) wartości dofitowanych współczynników prostej oraz ich niepewności
print("zad3")
def zad3(lista_x,lista_y):
    n=len(lista_x)
    sredniax=sum(lista_x)/n
    sredniay=sum(lista_y)/n
    D=sum((x-sredniax)**2 for x in lista_x)
    a=sum(map(lambda x,y: y*(x-sredniax),lista_x,lista_y))/D
    b=sredniay-a*sredniax
    deltay=math.sqrt(sum(map(lambda x,y: (y-(a*x+b))**2/(n-2),lista_x,lista_y)))
    deltaa=deltay/math.sqrt(D)
    deltab=deltay*math.sqrt(1/n + sredniax**2/D)
    return a,b,deltaa,deltab
list_x=[1,2,3,4,5,6]
list_y=[3,5,7,8,10,12]
print(zad3(list_x,list_y))
#zad4 Proszę napisać funkcję myreduce przyjmującą dwa parametry (funkcję i sekwencję) oraz zwracającą liczbę. Funkcja przekazywana jako parametr będzie funkcją przyjmującą dwa parametry. Działanie funkcji proszę przetestować korzystając z wyrażenia lambda dla dodawania i mnożenia
print("zad4")
def myreduce(fun,*iterat):
    listaa=list(iterat)
    while(len(listaa)>=2):
        listaa[len(listaa)-2]=fun(listaa[len(listaa)-2],listaa[len(listaa)-1])
        listaa.pop()
    return listaa[0]
print(myreduce(lambda x,y:x+y,1,2))
print(myreduce(lambda x,y:x*y,2,3))
#zad5 Proszę znaleźć:
#największą wartość w każdym wierszu macierzy (map),
#największą wartość w każdej kolumnie macierzy (map+zip),
#sumę dowolnej liczby macierzy (map+zip+lista składana)
print("zad5")
n=1
arr=[[random.randint(0,10) for j in range(5)] for i in range(5)]
print(arr)
k=3
print(list(map(lambda x:max(x),arr)))
print(list(map(lambda x:max(x),zip(*arr))))
print([list(map(lambda x: sum(x),zip(arr[i]))) for i in range(len(arr))])
