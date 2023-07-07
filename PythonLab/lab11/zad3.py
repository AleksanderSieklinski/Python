'''\nZad3 polega na utworzeniu klasy abstrakcyjnej calka oraz klas pochodnych Simpson i Monte Carlo, liczacych calki podanymi sposobami.\n'''
#3 Proszę napisać abstrakcyjną klasę Calka z metodą inicjalizacyjną określającą funkcję podcałkową 
# (przy wywołaniu proszę użyć wyrażenia lambda) oraz granice całkowania i metodą abstrakcyjną 
# obliczającą wartość całki (1p).
# Następnie proszę utworzyć klasy dziedziczące po klasie Calka z metodami obliczającymi wartość całki odpowiednio metodą:
# Simpsona (1.5p)
# Monte Carlo, proszę wykorzystać zaimplementowany generator liczb pseudolosowych (2.5p)
# Losujemy n punktów znajdujących się w obrębie prostokąta ograniczającego funkcję w granicach całkowania. 
# Wprowadzamy zmienną pomocniczą t, którą modyfikować będziemy następująco:
# jeżeli wylosowany punkt (xi, yi) leży nad osią OY i jednocześnie pod wykresem funkcji całkowanej, 
# czyli spełnia nierówność: 0 < yi ≤ f(xi), wówczas zwiększamy zmienną t o jeden,
# jeżeli wylosowany punkt (xi, yi) leży pod osią OY i jednocześnie nad wykresem funkcji całkowanej, 
# czyli spełnia nierówność: 0 > yi ≥ f(xi), wówczas zmniejszamy zmienną t o jeden,
# jeżeli wylosowany punkt (xi, yi) nie spełnia żadnego z powyższych warunków, wówczas pozostawiamy zmienną t bez zmian.
# Całkę obliczamy jako Pprostokątat/n

# Obliczenia prowadzimy, aż do osiągnięcia poprawnego wyniku (https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.quad.html) z zadaną dokładnością.

import math
import random
import zad2

class Calka:
    def __init__(self, funkcja, a, b):
        self.funkcja=funkcja
        self.a=a
        self.b=b
    def oblicz(self):
        pass

class Simpson(Calka):
    def oblicz(self,n):
        h=(self.b-self.a)/(2*n)
        wart=self.funkcja(self.a)+self.funkcja(self.b)
        for i in range(1,2*n):
            self.a+=h
            if i%2==0:
                wart+=2*self.funkcja(self.a)
            else:
                wart+=4*self.funkcja(self.a)
        return h/3*wart
        
from scipy import integrate
class MonteCarlo(Calka):
    def oblicz(self,eps=0.0001):
        t=0
        n=0
        porownanie=integrate.quad(self.funkcja, self.a, self.b)[0]
        while True:
            n+=1
            x=zad2.LiczbyLosowe(2**31-1,1,7**5,0).losuj()*(self.b-self.a)+self.a
            y=zad2.LiczbyLosowe().losuj()*(self.funkcja(self.b)-self.funkcja(self.a))+self.funkcja(self.a)
            if y<=self.funkcja(x) and y>=0:
                t+=1
            elif y>=self.funkcja(x) and y<=0:
                t-=1
            if abs((self.b-self.a)*t/n-porownanie)<eps:
                break
        return (self.b-self.a)*t/n
