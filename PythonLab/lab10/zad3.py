'''\nzadanie 3 polega na wykorzystaniu klasy Wektor3D do obliczenia strumienia indukcji E.M,
sily Lorentza oraz prace sily Lorentza\n'''
#3 Proszę utworzyć funkcje obliczające odpowiednio (jako parametry przekazujemy obiekty wcześniej utworzonej klasy) (1p):
# strumień indukcji magnetycznej: Φ=B•S
# siłę Lorentza F=q(E+v × B)
# pracę siły Lorentza W=qE•v

import zad2

def strumien_indukcji_magnetycznej(B, S):
    return B.iloczyn_skalarny(S)

def sila_lorentza(q, E, v, B):
    return (v.iloczyn_wektorowy(B)+E)*q

def praca_sily_lorentza(q, E, v):
    return q*E.iloczyn_skalarny(v)