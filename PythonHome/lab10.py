#1.1 Celem programu jest implementacja automatu komórkowego 2D "Gra w życie". Tworzy się go na siatce kwadratowej NxN. Każda komórka może być w jednym z dwóch stanów 1 (żywa) lub 0 (martwa). Stosujemy periodyczne warunki brzegowe ("spinamy" krawędzie).
# Reguły gry:
# martwa komórka, która ma dokładnie 3 żywych sąsiadów, staje się żywa w następnej iteracji
# żywa komórka z 2 albo 3 żywymi sąsiadami pozostaje nadal żywa; przy innej liczbie sąsiadów umiera
# Proszę utworzyć klasę, a w niej:
# metodę inicjalizującą przyjmującą trzy parametry całkowite, pierwszy parametr określa rozmiary siatki, drugi wielkość początkowego kwadratu wypełnionego jedynkami, a trzeci liczbę iteracji
# metodę ewaluacji automatu - w każdej iteracji ustalamy nowy stan każdej komórki, na podstawie stanku układu w kroku poprzednim
# metodę wypisującą na ekran stan układu - jeśli komórka jest żywa to wypisujemy znak '*', jeśli martwa to spacje
# proszę uruchomić program dla siatki 30x30 i "żywego" obszaru początkowego 10x10 oraz 11x11

print("Zadanie 1.1")

class Gra_w_zycie:
    def __init__(self, N, kwadrat, iteracje):
        self.N=N
        self.kwadrat=kwadrat
        self.iteracje=iteracje
        self.tablica=[]
        for i in range(N):
            self.tablica.append([])
            for j in range(N):
                self.tablica[i].append(0)
        for i in range(kwadrat):
            for j in range(kwadrat):
                self.tablica[i][j]=1
    def rysuj(self):
        for i in range(self.N):
            for j in range(self.N):
                if self.tablica[i][j]==1:
                    print("*", end=" ")
                else:
                    print("x", end=" ")
            print()
    def zapisz(self, nazwa):
        plik=open(nazwa, "w")
        for i in range(self.N):
            for j in range(self.N):
                if self.tablica[i][j]==1:
                    plik.write("*")
                else:
                    plik.write("x")
            plik.write("\n")
        plik.close()
    def wczytaj(self, nazwa):
        plik=open(nazwa, "r")
        i=0
        for linia in plik:
            for j in range(self.N):
                if linia[j]=="*":
                    self.tablica[i][j]=1
                else:
                    self.tablica[i][j]=0
            i+=1
        plik.close()
    def ewaluacja(self):
        for k in range(self.iteracje):
            tablica2=[]
            for i in range(self.N):
                tablica2.append([])
                for j in range(self.N):
                    tablica2[i].append(0)
            for i in range(self.N):
                for j in range(self.N):
                    suma=0
                    for k in range(-1,2):
                        for l in range(-1,2):
                            if self.tablica[(i+k)%self.N][(j+l)%self.N]==1:
                                suma+=1
                    if self.tablica[i][j]==1:
                        suma-=1
                        #if suma>=2:
                        if suma==2 or suma==3:
                            tablica2[i][j]=1
                        else:
                            tablica2[i][j]=0
                    else:
                        if suma==3:
                            tablica2[i][j]=1
                        else:
                            tablica2[i][j]=0
            self.tablica=tablica2
            #self.rysuj()
            #print()

ile=20
gra = Gra_w_zycie(30,10,ile)
gra.ewaluacja()
gra.zapisz("gra.txt")

#1.2 Celem programu jest implementacja tzw. automatu komórkowego. Składa się on z N komórek, każda w stanie 0 lub 1. W kolejnych iteracjach stan danej komórki zmienia się zgodnie z określoną regułą, na podstawie stanu danej komórki oraz jej dwóch najbliższych sąsiadów (prawego i lewego) w poprzedniej iteracji.
# Regułę zapisuje się jako binarną reprezentację liczby zapisanej w systemie dziesiętnym, np. dla reguły nr 30 kek reprezentacja binarna to 00011110. Jeżeli każda komórka może być w dwóch stanach (0 lub 1), to możliwych jest osiem kombinacji stanu komórki i jej dwóch najbliższych sąsiadów.
# Możemy utworzyć tabelę, w górnym wierszu której przedstawiony jest stan danej komórki i jej dwóch najbliższych sąsiadów (lewy sąsiad, komórka, prawy sąsiad), a w wierszu dolnym wpisujemy regułę automatu, która określa stan komórki centralnej w chwili kolejnej
# (przyjmujemy periodyczne warunki brzegowe - lewym sąsiadem komórki o indeksie - jest komórka o indeksie N-1, prawym sąsiadem komórki o indeksie N-1 jest komórka o indeksie 0).
# Przykład:
#t = 0: 0000000001000000000
#t = 1: 0000000011100000000
#t = 2: 0000000110010000000
#t = 3: 0000001101110000000
# Proszę utworzyć klasę Automat, a w niej:
# metodę inicjalizującą przyjmującą dwa parametry całkowite i jeden logiczny, pierwzsy parametr określa liczbę komórek, drugi regułę automatu, trzeci określa stan początkowy: losowy bądź zera z wyjątkiem komórki w środku, równej 1
# metodę ewolucji automatu z parametrem określającym liczbę iteracji
# metodę wypisującą na ekran przebieg ewolucji (zamiast jedynek proszę wyświetlić *, a zamiast zer - spacje)
# Proszę uruchomić program dla automatu o długości 31, dla reguł 90,94 i 182 oraz 16 iteracji.
print("Zadanie 1.2")

import random

class Automat:
    def __init__(self, N, regula, stan_poczatkowy):
        self.N=N
        self.regula=regula
        self.stan_poczatkowy=stan_poczatkowy
        self.tablica=[]
        for i in range(self.N):
            self.tablica.append(0)
        if self.stan_poczatkowy==True:
            for i in range(self.N):
                self.tablica[i]=random.randint(0,1)
        else:
            for i in range(self.N):
                self.tablica[i]=0
            self.tablica[self.N//2]=1
    def ewolucja(self, iteracje):
        for k in range(iteracje):
            tablica2=[]
            for i in range(self.N):
                tablica2.append(0)
            for i in range(self.N):
                suma=0
                for j in range(-1,2):
                    suma+=self.tablica[(i+j)%self.N]
                if self.tablica[i]==1:
                    suma-=1
                    if self.regula&(1<<suma):
                        tablica2[i]=1
                    else:
                        tablica2[i]=0
                else:
                    if self.regula&(1<<suma):
                        tablica2[i]=1
                    else:
                        tablica2[i]=0
            self.tablica=tablica2
            self.rysuj()
    def rysuj(self):
        for i in range(self.N):
            if self.tablica[i]==1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

automat1=Automat(31, 90, False)
automat1.ewolucja(16)

#2 Proszę utworzyć klasę Wektor3D, którego stan początkowy jest określony przez metodę inicjalizacyjną.W klasie proszę zdefiniować metody przeciążające operatory dodawania,odejmowania,mnożenia(mnożenie wektora przez liczbę) oraz metodę str.
# Proszę napisać także metody zwracającego odpowiednipo długość wektora, iloczyn skalarny, wektorowy i mieszany.
print("Zadanie 2")

class Wektor3D:
    def __init__(self, x, y, z):
        self.x=x
        self.y=y
        self.z=z
    def __add__(self, other):
        return Wektor3D(self.x+other.x, self.y+other.y, self.z+other.z)
    def __sub__(self, other):
        return Wektor3D(self.x-other.x, self.y-other.y, self.z-other.z)
    def __mul__(self, other):
        return Wektor3D(self.x*other, self.y*other, self.z*other)
    def __str__(self):
        return f'({self.x}, {self.y}, {self.z})'
    def dlugosc(self):
        return (self.x**2+self.y**2+self.z**2)**(1/2)
    def iloczyn_skalarny(self, other):
        return self.x*other.x+self.y*other.y+self.z*other.z
    def iloczyn_wektorowy(self, other):
        return Wektor3D(self.y*other.z-self.z*other.y, self.z*other.x-self.x*other.z, self.x*other.y-self.y*other.x)
    def iloczyn_mieszany(self, other, other2):
        return self.iloczyn_skalarny(other.iloczyn_wektorowy(other2))
    
w1=Wektor3D(1,2,3)
w2=Wektor3D(4,5,6)
print(w1)
print(w2)
print(w1+w2)
print(w1-w2)
print(w1*2)
print(w1.dlugosc())
print(w1.iloczyn_skalarny(w2))
print(w1.iloczyn_wektorowy(w2))
print(w1.iloczyn_mieszany(w2, w1))

#3 Proszę utworzyć funkcje obliczające odpowiednio(jako parametry przekazujemy obiekty wcześniej utworzonej klasy Wektor3D):
# strumień indukcji magnetycznej: B*s
# siłę Lorentza: F=q*(v x B)
# pracę siły Lorentza: W=q*E*v
print("Zadanie 3")

def strumien_indukcji_magnetycznej(B, s):
    return B.x*s.x+B.y*s.y+B.z*s.z
def sila_lorentza(q, v, B):
    return q.iloczyn_wektorowy(v.iloczyn_wektorowy(B))
def praca_sily_lorentza(q, E, v):
    return q.iloczyn_skalarny(E.iloczyn_wektorowy(v))

print(strumien_indukcji_magnetycznej(w1, w2))
print(sila_lorentza(w1, w2, w1))
print(praca_sily_lorentza(w1, w2, w1))