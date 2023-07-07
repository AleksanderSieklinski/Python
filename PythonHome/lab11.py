#1 Proszę napisać iterator zwracający kolejne liczby pierwsze z zadanego zakresu dwoma sposobami i porównać ich wykorzystanie
print("Zadanie 1")

class LiczbyPierwsze:
    def __init__(self, start, stop):
        self.start=start
        self.stop=stop
        self.liczba=start
    def __iter__(self):
        self.liczba=self.start
        return self
    def __next__(self):
        if self.liczba<self.stop:
            for i in range(2, self.liczba):
                if self.liczba%i==0:
                    self.liczba+=1
                    return self.__next__()
            self.liczba+=1
            return self.liczba-1
        else:
            raise StopIteration
        
lp1 = LiczbyPierwsze(1, 100)
lp2 = LiczbyPierwsze(1, 100)
print("Pierwszy sposob:")
for i in lp1:
    print(i, end=" ")
print("\nDrugi sposob:")
for i in range(26):
    print(next(lp2), end=" ")
print()
#2 Proszę napisać iterator liczb pseudolosowych. Ciąg taki otrzymujemy ze wzoru: Xn+1 = (aXn + c) mod m, dla m = 2^31-1, a = 7^5,c = 0,x0 = 1.
# Korzystając z zaimplementowanego iteratora proszę wylosować 10^5 par liczb z przedziału [0,1]. Proszę sprawdzić jaki procent wylosowanych par mieści się w kwadracie o boku 0.1*n, gdzie n nalezy do przedzialu [1,10].
# Otrzymany wynik proszę porównać z wynikiem uzyskiwanym z wykorzysaniem generatora liczb pseudolosowych z jezyka Python.
print("Zadanie 2")

import random

class Pseudolosowe:
    def __init__(self, n):
        self.n=n
        self.x=1
        self.m=2**31-1
        self.a=7**5
        self.c=0
    def __next__(self):
        self.x=(self.a*self.x+self.c)%self.m
        return self.x/self.m
    def __iter__(self):
        return self
    
p1=Pseudolosowe(100000)
licznik=0
for i in range(100000):
    if next(p1)<0.1:
        licznik+=1
print(licznik/100000)
print("Generator Pythona:")
licznik=0
for i in range(100000):
    if random.random()<0.1:
        licznik+=1
print(licznik/100000)

# Proszę napisać abstrakcyjną klasę Calka z metoda inicjalizacyjna okreslajaca funkcje podcalkowa oraz granice calkowania i metode abstrakcyjna obliczajaca calke.
# Następnie prosze utworzyć klasy dziedziczące po klasie Calka z metodami obliczajacymi wartość całki odpowiednią metodą.
# Simspona: h=(xk-xp)/2n, s=h/3*(f(0)+4(f(1)+f(3)+...+f(2n-1))+2(f(2)+f(4)+...+f(2n-2))+f(2n))
# Monte Carlo, proszę wykorzystać zaimplementowany generator liczb pseudolosowych z poprzedniego zadania.
# losujemy n punktów znajdujących się w obrębie prostokąta ograniczającego funkcję w granicach całkowania. Wprowadzamy zmienną pomocniczą t, którą modyfikować będziemy następująco:
# jeżeli wylosowany punkt (xi,yi) leży nad osią OY i jednocześnie pod wykresem funkcji całkowanej, czyli spełnia nierówność 0 < yi < f(xi), to zwiększamy zmienną t o 1.
# jeżeli wylosowany punkt (xi,yi) leży pod osią OY i jednocześnie nad wykresem funkcji całkowanej, czyli spełnia nierówność 0 > yi > f(xi), to zmniejszamy zmienną t o 1.
# jeżeli wylosowany punkt (xi,yi) nie spełnia żadnego z powyższych warunków, to nie modyfikujemy zmiennej t.
# Całkę obliczamy jako Pprostokąta t/n.
# Obliczenia prowadzimy aż do osiągnięcia poprawnego wyniku z dokładnością do 3 miejsc po przecinku.
print("Zadanie 3")

import math

class Calka:
    def __init__(self, funkcja, a, b):
        self.funkcja=funkcja
        self.a=a
        self.b=b
    def oblicz(self):
        pass

class Simpson(Calka):
    def oblicz(self):
        n=1000
        h=(self.b-self.a)/(2*n)
        suma1=0
        suma2=0
        for i in range(1, 2*n):
            if i%2==0:
                suma2+=self.funkcja(self.a+i*h)
            else:
                suma1+=self.funkcja(self.a+i*h)
        return h/3*(self.funkcja(self.a)+4*suma1+2*suma2+self.funkcja(self.b))
    
class MonteCarlo(Calka):
    def oblicz(self):
        n=1000
        t=0
        for i in range(n):
            x=random.random()*(self.b-self.a)+self.a
            y=random.random()
            if y>0 and y<self.funkcja(x):
                t+=1
            elif y<0 and y>self.funkcja(x):
                t-=1
        return t/n*(self.b-self.a)
    
def funkcja(x):
    return math.sin(x)

s=Simpson(funkcja, 0, math.pi)
print(s.oblicz())
m=MonteCarlo(funkcja, 0, math.pi)
print(m.oblicz())
from scipy import integrate
print(integrate.quad(funkcja, 0, math.pi)[0])