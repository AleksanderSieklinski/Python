'''\nZad2 sprawdza poprawnosc numeru PESEL.
Jako dane wejsciowe przyjmuje pesel,date urodzenia oraz plec,
a jako wynik zwraca napis ze pesel jest poprawny lub ValueError\n'''
#2
#Funkcję sprawdzającą poprawność numeru PESEL (3p)
#Parametrami wejściowymi do funkcji są: Pesel, data urodzenia (datetime.date) oraz płeć.
#Przykłady:
#    02070803628, 8 lipca 1902, kobieta
#    02270803624, 8 lipca 2002, kobieta
#    02270812350, 8 lipca 2002, mężczyzna
#PESEL
#    cyfry 1-2 to ostatnie dwie cyfry roku urodzenia
#    cyfry 3-4 to dwie cyfry miesiąca urodzenia
#    cyfry 5-6 to dwie cyfry dnia urodzenia
#    cyfry 7-10 liczba porządkowa z oznaczeniem płci (liczba parzysta - kobieta, liczba nieparzysta - mężczyzna)
#    cyfra 11 suma kontrolna

#Do numeru miesiąca dodawane są następujące wartości w zależności od roku:

#    dla lat 1800 - 1899 - 80
#    dla lat 1900 - 1999 - 0
#    dla lat 2000 - 2099 - 20
#    dla lat 2100 - 2199 - 40
#    dla lat 2200 - 2299 - 60

#Suma kontrolna: każdą pozycję numeru ewidencyjnego mnoży się przez odpowiednią wagę, są to kolejno: 1 3 7 9 1 3 7 9 1 3 i sumuje.
#Wynik dzieli się modulo 10 i otrzymaną wartość należy odjąć od 10 i znów podzielić modulo 10.
#Otrzymana wartość powinna być zgodna z ostatnią cyfrą numeru PESEL.
#Wyjątek zgłaszamy w przypadku kiedy parametr przekazany do funkcji nie składa się z samych cyfr, ma niepoprawną długość, cokolwiek innego się nie zgadza.

import datetime as data

def zad2(pesel, data, plec):
    if len(pesel)!=11:
        raise ValueError("Zly format")
    elif int(pesel[4:6]) > 31:
        raise ValueError("Zly format")
    elif int(pesel[9]) % 2 == 0 and plec == "mezczyzna":
        raise ValueError("Zly format")
    elif int(pesel[9]) % 2 == 1 and plec == "kobieta":
        raise ValueError("Zly format")
    if data.year > 1800 and data.year < 1899:
        add = 1800
        addmonth = 80
        if data.month != int(pesel[2:4]) - 80:
            raise ValueError(1800)
    elif data.year > 1900 and data.year < 1999:
        add = 1900
        addmonth = 0
        if data.month != int(pesel[2:4]):
            raise ValueError(1900)
    elif data.year > 2000 and data.year < 2099:
        add = 2000
        addmonth = 20
        if data.month != int(pesel[2:4]) - 20:
            raise ValueError(2000)
    elif data.year > 2100 and data.year < 2199:
        add = 2100
        addmonth = 40
        if data.month != int(pesel[2:4]) - 40:
            raise ValueError(2100)
    elif data.year > 2200 and data.year < 2299:
        add = 2200
        addmonth = 60
        if data.month != int(pesel[2:4]) - 60:
            raise ValueError(2200)
    if data.day != int(pesel[4:6]):
        raise ValueError("Dzien")
    elif data.month != (int(pesel[2:4]) - addmonth):
        raise ValueError("Miesiac")
    elif data.year != (int(pesel[0:2]) + add):
        raise ValueError("Rok")
    suma = 0
    weight = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    for i in range(10):
        suma += int(pesel[i]) * weight[i]
    suma = (10 - suma % 10)%10
    if suma != int(pesel[10]):
        raise ValueError("Niepoprawna wartosc kontrolna")
    print("Pesel poprawny")