'''\nZad4 polega na utworzeniu dekoratora jako klase, ktory bedzie zliczal wywolania funkcji oblozonych dekoratorem, z metoda statyczna zwracajaca wynik.\n'''
#4 Proszę utworzyć dekorator (implementowany jako klasa) umożliwiający zliczenie liczby wywołań 
# poszczególnych funkcji obłożonych dekoratorem, z metodą statyczną zwracającą wynik
import zad1
import zad2
import zad3

class Dekorator:
    count={}
    def __init__(self,func):
        Dekorator.count[func.__name__]=0
        self.func=func
    def __call__(self,*args):
        Dekorator.count[self.func.__name__]+=1
        return self.func(*args)
    @staticmethod
    def wynik():
        print("Wywolania funkcji: ",Dekorator.count)

@Dekorator
def dodawanie(self,other):
    return zad2.dodawanie(self,other)
@Dekorator
def odejmowanie(self,other):
    return zad2.odejmowanie(self,other)
@Dekorator
def obwod(*args):
    return zad3.Figura.obwod(*args)
@Dekorator
def pole(*args):
    return zad3.Figura.pole(*args)
