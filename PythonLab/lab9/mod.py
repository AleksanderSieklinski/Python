#Poszczególne wywołania funkcji oraz wyniki ich działania proszę logować (1p).
if __name__=='__main__':
    import logging
    import sys
    import os
    import time
    open('mod.log', 'w').close()
    logging.basicConfig(filename='mod.log', level=logging.DEBUG)
    logging.info('Start')

    import datetime
    import zad1
    print(zad1.__doc__)
    zad1
    try:
        zad1.zad1("924803")
        logging.info('924803 jest poprawnym numerem karty')
    except:
        print("Zly numer karty")
        logging.info('924803 jest niepoprawnym numerem karty')
    try:
        zad1.zad1("1234567898765437")
        logging.info('1234567898765437 jest poprawnym numerem karty')
    except:
        print("Zly numer karty")
        logging.info('1234567898765437 jest niepoprawnym numerem karty')
    try:
        zad1.zad1("1234567891234564")
        logging.info('1234567891234564 jest poprawnym numerem karty')
    except:
        print("Zly numer karty")
        logging.info('1234567891234564 jest niepoprawnym numerem karty')
    try:
        zad1.zad1("1234567891234563")
        logging.info('1234567891234563 jest poprawnym numerem karty')
    except:
        logging.info('1234567891234563 jest niepoprawnym numerem karty')
        print("Zly numer karty")
    import zad2
    print(zad2.__doc__)
    zad2
    try:
        zad2.zad2("02070803628",datetime.date(1902, 7, 8), "kobieta")
        logging.info('02070803628, 8 lipca 1902, kobieta jest poprawnym peselem')
    except:
        print("Zly numer pesel")
        logging.info('02070803628, 8 lipca 1902, kobieta jest niepoprawnym peselem')
    try:
        zad2.zad2("02270803624",datetime.date(2002, 7, 8), "kobieta")
        logging.info('02270803624, 8 lipca 2002, kobieta jest poprawnym peselem')
    except:
        print("Zly numer pesel")
        logging.info('02270803624, 8 lipca 2002, kobieta jest niepoprawnym peselem')
    try:
        zad2.zad2("02270812350",datetime.date(2002, 7, 8), "mężczyzna")
        logging.info('02270812350, 8 lipca 2002, mężczyzna jest poprawnym peselem')
    except:
        print("Zly numer pesel")
        logging.info('02270812350, 8 lipca 2002, mężczyzna jest niepoprawnym peselem')
    import zad3
    print(zad3.__doc__)
    zad3
    try:
        zad3.zad3("liberalny","daty.in")
        logging.info('daty.in jest poprawnym plikiem')
    except:
        print("Conajmniej jedna wartosc w pliku jest niepoprawna")
        logging.info('daty.in jest niepoprawnym plikiem')
    logging.info('Stop')