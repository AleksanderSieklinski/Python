'''\nZad1 polega na stworzeniu klasy implementujacej stos oraz stos posortowany.\n'''
#1 Proszę utworzyć
# Klasę implementującą stos, który można zainicjalizować przekazując zmienną liczbę parametrów, listę lub inny stos. 
# Sprawdzenie typu i odpowiednią inicjalizację proszę wykonać korzystając z konstrukcji match-case. W klasie proszę zdefiniować metodę pozwalającą na dodanie elementu do stosu oraz metodę pozwalającą na jego wypisanie. 
# Proszę przetestować działanie klasy (2p).
# Klasę implementującą stos posortowany, dziedziczącą po wcześniej zdefiniowanej klasie. Inicjalizacja jak wcześniej oraz posortowanym stosem, przy czym przed sortowaniem proszę zachować elementy typu najliczniej reprezentowanego.
# W klasie proszę zdefiniować metodę pozwalającą na dodanie elementu pod warunkiem, że zachowa to porządek sortowania.
# Proszę sprawdzić jaki jest średni rozmiar posortowanego stosu, który wypełniamy całkowitymi liczbami losowymi z przedziału [0,100] losując 100 wartości (średnia po 100 powtórzeniach) (2p).

class Stos:
    def __init__(self,*args):
        for arg in args:
            match arg:
                case list():
                    self.stos = arg
                case Stos():
                    self.stos = arg.stos
                case _:
                    self.stos = list(args)
    def dodaj(self,element):
        self.stos.append(element)
    def wypisz(self):
        print(self.stos)

class StosPosortowany(Stos):    
    def __init__(self,*args):
        Stos.__init__(self,*args)
        self.ileint = 0
        self.ilestr = 0
        self.ilefloat = 0
        for arg in args:
            match arg:
                case int():
                    self.ileint += 1
                case str():
                    self.ilestr += 1
                case float():
                    self.ilefloat += 1
        if self.ileint >= self.ilestr and self.ileint >= self.ilefloat:
            self.stos.sort(key=int)
        elif self.ilestr >= self.ileint and self.ilestr >= self.ilefloat:
            self.stos.sort(key=str)
        elif self.ilefloat >= self.ileint and self.ilefloat >= self.ilestr:
            self.stos.sort(key=float)

    def dodaj(self,element):
        if type(element) == type(self.stos[0]):
            if element > self.stos[-1]:
                self.stos.append(element)
        else:
            print("Nie mozna dodac elementu do stosu")

