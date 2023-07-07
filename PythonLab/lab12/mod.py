if __name__=='__main__':
    import logging
    import sys
    import os
    import time
    import datetime
    from scipy import integrate
    import math

    open('mod.log', 'w').close()
    logging.basicConfig(filename='mod.log', level=logging.DEBUG)
    logging.info('Start')

    import zad1
    print(zad1.__doc__)
    zad1

    try:
        punkt1 = zad1.Punkt()
        print("Punkt1:", punkt1.x, punkt1.y)
    except:
        print("Blad iteracji, koniec zakresu")
        logging.info("Blad iteracji w liczbach pierwszych, koniec zakresu")

    import zad2
    print(zad2.__doc__)
    zad2
    import random
    try:
        punkt2 = zad1.Punkt()
        punkt3 = zad1.Punkt()
        punkt2.x = 2
        punkt2.y = 2
        punkt3.x = 3
        punkt3.y = 3
        print("Punkt2:", punkt2.x, punkt2.y)
        print("Punkt3:", punkt3.x, punkt3.y)
        zad2.dodawanie(punkt2,punkt3)
        print("Dodawanie punktu 2 i 3:", punkt2.x, punkt2.y)
        zad2.odejmowanie(punkt2,punkt3)
        print("Odejmowanie punktu 2 i 3:", punkt2.x, punkt2.y)
    except:
        print("Wynik poza zadanym zakresem")
        logging.info("Wynik poza zadanym zakresem")

    import zad3
    print(zad3.__doc__)
    zad3
    try:
        punkt4 = zad1.Punkt()
        punkt5 = zad1.Punkt()
        punkt6 = zad1.Punkt()
        punkt7 = zad1.Punkt()
        punkt4.x,punkt4.y,punkt5.x,punkt5.y,punkt6.x,punkt6.y,punkt7.x,punkt7.y = 1,0,1,1,0,1,0,0
        print("Punkt4:", punkt4.x, punkt4.y)
        print("Punkt5:", punkt5.x, punkt5.y)
        print("Punkt6:", punkt6.x, punkt6.y)
        print("Punkt7:", punkt7.x, punkt7.y)
        print("Obwod czworokata:", zad3.Figura.obwod(punkt4,punkt5,punkt6,punkt7))
        print("Pole czworokata:", zad3.Figura.pole(punkt4,punkt5,punkt6,punkt7))
        print("Obwod trojkata:", zad3.Figura.obwod(punkt4,punkt5,punkt6))
        print("Pole trojkata:", zad3.Figura.pole(punkt4,punkt5,punkt6))
    except:
        print("Nieprawidlowe wspolrzedne")
        logging.info("Nieprawidlowe wspolrzedne")
    import zad4
    print(zad4.__doc__)
    zad4
    try:
        zad4.dodawanie(punkt2,punkt3)
        zad4.odejmowanie(punkt2,punkt3)
        zad4.obwod(punkt4,punkt5,punkt6,punkt7)
        zad4.pole(punkt4,punkt5,punkt6,punkt7)
        zad4.obwod(punkt4,punkt5,punkt6)
        zad4.pole(punkt4,punkt5,punkt6)
        zad4.Dekorator.wynik()
    except:
        print("Blad wywolan")
        logging.info("Blad wywolan")
    logging.info('Stop')
