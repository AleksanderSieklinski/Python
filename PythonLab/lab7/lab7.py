#1 (2p) Proszę napisać generator zwracający kolejne wiersze trójkąta Pascala wraz z sumą ich wartości
print("Zadanie 1")
def pascal():
    row = [1]
    i=0
    while i<10:
        yield row, sum(row)
        row = [1] + [row[i] + row[i+1] for i in range(len(row)-1)] + [1]
        i+=1

ile=20
for i in pascal():
    for j in range(ile):
        print(" ", end="")
    if ile%2==0:
        ile-=1
    else:
        ile-=2
    print(i)
    if i[0][0] == 10:
        break

#2 (2p) Proszę wygenerować losowy ciąg zer i jedynek o długości N. Proszę napisać generator zwracający liczbę zer oddzielających 
#kolejne jedynki w sekwencji przekazanej jako parametr. Korzystając z utworzonego generatora proszę obliczyć średnią odległość między kolejnymi jedynkami w wygenerowanym wcześniej ciągu
print("Zadanie 2")

import random

def zeros(seq):
    i=1
    for j in seq:
        if j==0:
            i+=1
        else:
            yield i
            i=1

N=10000
seq=[random.randint(0,1) for i in range(N)]
print(sum(zeros(seq))/N)

#3  Proszę napisać trzy funkcje generatorowe:
#zwracającą kolejne elementy ciągu Fibonacciego (nieskończony),
#zwracającą te wartości z przekazanej jako parametr sekwencji, które są parzyste/nieparzyste
#zwracającą wartości z przekazanej jako pierwszy parametr sekwencji i przerywającą działanie po napotkaniu wartości większej niż drugi parametr przekazany do funkcji
#Korzystając ze zdefiniowanych funkcji proszę obliczyć sumę parzystych/nieparzystych elementów ciągu Fibonacciego mniejszych od 100
print("Zadanie 3")

def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b

def evenodd(seq,n):
    for i in seq:
        if i%2==n:
            yield i

def more_than(seq,n):
    for i in seq:
        if i>n:
            break
        yield i

print(sum(more_than(evenodd(fib(),0),100)))
print(sum(more_than(evenodd(fib(),1),100)))
#4 (2p) Proszę napisać generator działający dokładnie tak samo jak wbudowany range (proszę się upewnić, że wiecie Państwo jak on działa!), ale pozwalający na generowanie liczb rzeczywistych
print("Zadanie 4")

def my_range(*args):
    if len(args)==1:
        start=0.
        stop=float(args[0])
        step=1.
    elif len(args)==2:
        start=args[0]
        stop=float(args[1])
        step=1.
    elif len(args)==3:
        start=float(args[0])
        stop=float(args[1])
        step=float(args[2])
    if stop<0 or start>stop:
        step=-step
    if step>0:
        while start<stop:
            yield start
            start+=step
    elif step<0:
        while start>stop:
            yield start
            start+=step
print("my_range(7)")
for i in my_range(7):
    print(i)
print("my_range(-7)")
for i in my_range(-7):
    print(i)
print("my_range(2,7)")
for i in my_range(2,7):
    print(i)
print("my_range(7,2)")
for i in my_range(7,2):
    print(i)
print("my_range(2,7,2)")
for i in my_range(2,7,2):
    print(i)
print("my_range(2,7,-2)")
for i in my_range(2,7,-2):
    print(i)
print("my_range(7,2,2)")
for i in my_range(7,2,2):
    print(i)
print("my_range(7,2,-2)")
for i in my_range(7,2,-2):
    print(i)
#5 2p) Proszę utworzyć generator zwracający odległość od punktu początkowego po N krokach dN=n1−n2=2n1−N
# (n1
# - liczba kroków wykonanych w prawo, n2
# liczba kroków wykonanych w lewo), dla błądzenia losowego w jednym wymiarze: wykonujemy N kroków o równej długości wzdłuż prostej, przyjmując jednakowe prawdopodobieństwo p wykonania kroku w prawo lub w lewo.
#Proszę sporządzić histogram odległości uzyskanej po N=20
# krokach dla 106
# powtórzeń i porównać z wartością oczekiwaną:
print("Zadanie 5")


import math

def random_walk(N):
    while True:
        n1=0
        n2=0
        for i in range(N):
            if random.random()>0.5:
                n1+=1
            else:
                n2+=1
        yield n1-n2

N=20
npowt=1000000
hist={}
walk=random_walk(N)
for i in range(npowt):
    j=next(walk)
    if j in hist:
        hist[j]+=1
    else:
        hist[j]=1
hist = {k: hist[k] for k in sorted(hist)}
#print(hist)
factn=math.factorial(N)
wart_ocz={}
for d in hist:
    factk=math.factorial((d+N)//2)
    factnk=math.factorial(N-(d+N)//2)
    wart_ocz[d]=(factn/(factnk*factk))/(2**N)

#print(wart_ocz)

import matplotlib.pyplot as plt
s=sum(hist.values())
s1=sum(wart_ocz.values())
plt.plot(hist.keys(), [v/s for v in hist.values()],'-')
plt.plot(wart_ocz.keys(),[v/s1 for v in wart_ocz.values()],'*')
plt.show()
