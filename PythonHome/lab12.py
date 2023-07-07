#1 Proszę utworzyć klasę definiującą współrzędne punktu na płaszczyźnie. Obie współrzędne proszę zdewfiniować jako własności (metoda inicjalizacyjna bezparametrowa) 
print("Zadanie 1")

class Punkt:
    def __init__(self):
        self.x=0
        self.y=0

#2 Proszę zdefiniować funkcje dodawania i odejmowania współrzednych (z wykorzystaniem wcześniej zdefiniowanej klasy) oraz opatrzyć je dekoratorem (implementowanym jako funkcja) sprawdzającym czy leżą w określonym zakresie, jeżeli nie - proszę zgłosić wyjątek.

def sprawdz_zakres(funkcja):
    def wrapper(self, other):
        if self.x+other.x>100 or self.x+other.x<0 or self.y+other.y>100 or self.y+other.y<0: #problem z tym jak suma odejmowan wieksza od 100
            raise ValueError("Wspolrzedne poza zakresem")
        else:
            return funkcja(self, other)
    return wrapper

@sprawdz_zakres
def dodawanie(self, other):
    self.x+=other.x
    self.y+=other.y
    return self

@sprawdz_zakres
def odejmowanie(self, other):
    self.x-=other.x
    self.y-=other.y
    return self

p1 = Punkt()
p2 = Punkt()
p1.x = 10
p1.y = 20
p2.x = 30
p2.y = 30
print("P1")
print(p1.x, p1.y)
print("P2")
print(p2.x, p2.y)
print("Dodawanie")
p1 = dodawanie(p1, p2)
print(p1.x, p1.y)
print("Odejmowanie")
p1 = odejmowanie(p1, p2)
print(p1.x, p1.y)

#3 Proszę utworzyć klasę z metodami statycznymi obliczającymi obwód i pole trójkąta lub czworokąta (dających się wpisać w okrąg, odpowiednio wzory Herona i Brahmagupty), zdefiniowanych poprzez współrzędne wierzchołków (klasa z zadania 1).
# Wzór Herona: P = sqrt(p(p-a)(p-b)(p-c)), gdzie p = polowa obwodu
# Wzór Brahmagupty: P = sqrt((p-a)(p-b)(p-c)(p-d)), oznaczenia jak wyżej
print("Zadanie 3")

class Figura:
    @staticmethod
    def obwod(a, b, c, d=None):
        if d==None:
            return a+b+c
        else:
            return a+b+c+d

    @staticmethod
    def pole(a, b, c, d=None):
        if d==None:
            p = (a+b+c)/2
            return (p*(p-a)*(p-b)*(p-c))**(1/2)
        else:
            p = (a+b+c+d)/2
            return (p*(p-a)*(p-b)*(p-c)*(p-d))**(1/2)
        
print("Trojkat")
print("Obwod")
print(Figura.obwod(3, 4, 5))
print("Pole")
print(Figura.pole(3, 4, 5))
print("Czworokat")
print("Obwod")
print(Figura.obwod(3, 4, 5, 6))
print("Pole")
print(Figura.pole(3, 4, 5, 6))

#4 Proszę utworzyć dekorator(implementowany jako klasa) umożliwiający zliczenie liczby wywołań poszczególnych funkcji obłożonych dekoratorem, z metodą statyczną zwracającą wynik.
print("Zadanie 4")

class Liczba:
    count = {}
    
    def __init__(self, func):
        self.func = func
        self.count[func.__name__] = 0
        
    def __call__(self, *args, **kwargs):
        self.count[self.func.__name__] += 1
        return self.func(*args, **kwargs)
    
    @staticmethod
    def get_counts():
        return Liczba.count

@Liczba
def HW():
    print("Hello, world!")

@Liczba
def GW():
    print("Goodbye, world!")
    
HW()  # wywołanie funkcji foo
GW()  # wywołanie funkcji bar
HW()  # ponowne wywołanie funkcji foo

counts = Liczba.get_counts()  # pobranie liczby wywołań
print(counts)  # {'foo': 2, 'bar': 1}

