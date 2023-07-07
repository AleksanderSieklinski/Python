if __name__=='__main__':
    import logging
    import sys
    import os
    import time
    import random
    open('mod.log', 'w').close()
    logging.basicConfig(filename='mod.log', level=logging.DEBUG)
    logging.info('Start')

    import zad1
    print(zad1.__doc__)
    zad1
    try:

        print("Stos")
        stos = zad1.Stos(1,2,3,4,5)
        stos.wypisz()
        stos.dodaj(6)
        stos.wypisz()
        stos2 = zad1.Stos(stos)
        print("Stos jako argument")
        stos2.wypisz()
        print("Stos posortowany")
        stos = zad1.StosPosortowany(1,2,3,4,5)
        stos.wypisz()
        stos.dodaj(6)
        stos.wypisz()
        stos.dodaj(1)
        stos.wypisz()
    except Exception as e:
        logging.exception(e)
        print(e)
    import zad2
    print(zad2.__doc__)
    zad2
    logging.info('Stop')
