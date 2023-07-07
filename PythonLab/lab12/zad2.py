'''\nZad2 polega na utworzeniu funkcji dodawania i odejmowania wspolrzednych z zadania 1 opatrzonych dekoratorem.\n'''
#2 Proszę zdefiniować funkcje dodawania i odejmowania współrzędnych 
# (z wykorzystaniem wcześniej zdefiniowanej klasy) oraz opatrzyć je dekoratorem 
# (implementowanym jako funkcja) sprawdzającym czy współrzędne leżą w określonym zakresie, 
# jeżeli nie - proszę zgłosić wyjątek
import zad1

def dekorator(xowe,yowe):
    def parametry(func):
        def wrapper(self,other):
            if self.x + other.x > xowe or self.y + other.y > yowe:
                raise ValueError("Wspolrzedne poza zakresem")
            return func(self,other)
        return wrapper
    return parametry
@dekorator(30,30)
def dodawanie(self,other):
    self.x += other.x
    self.y += other.y
    return self
@dekorator(30,30)
def odejmowanie(self,other):
    self.x -= other.x
    self.y -= other.y
    return self
