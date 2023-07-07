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
        lp1=zad1.LiczbyPierwsze(2,100)
        ile=0
        print("Pierwszy sposob, iterujemy w petli po obiektach")
        for i in lp1:
            print(i)
        lp2=zad1.LiczbyPierwsze(2,100)
        print("Drugi sposob, wywolanie next")
        for i in range(2,100):
            print(lp2.__next__())
    except:
        print("Blad iteracji, koniec zakresu")
        logging.info("Blad iteracji w liczbach pierwszych, koniec zakresu")

    import zad2
    print(zad2.__doc__)
    zad2
    import random
    try:
        ll1=zad2.LiczbyLosowe()
        ile1,ile2=0,0
        n=[0.1*i for i in range(1,11)]
        print("Pierwsza wartosc to procent wylosowanych par z iteratora, druga to procent wylosowanych par z random.random()")
        for j in n:
            print("\nDla n=",j*10,sep="")
            ile1=0
            ile2=0
            for i in range(105):
                if next(ll1)<j:
                    ile1+=1
                if random.random()<j:
                    ile2+=1
            print(round(ile1/105,2),"%",sep="")
            print(round(ile2/105,2),"%",sep="")
    except:
        print("Blad iteracji")
        logging.info("Blad iteracji w liczbach pseudolosowych")

    import zad3
    print(zad3.__doc__)
    zad3
    print("Calka z 2x w przedziale [0,pi] metoda Simpsona")
    zad3.calka1=zad3.Simpson(lambda x: 2*x, 0, math.pi)
    print(zad3.calka1.oblicz(10000))
    print("Calka z 2x w przedziale [0,pi] metoda Monte Carlo")
    zad3.calka2=zad3.MonteCarlo(lambda x: 2*x, 0, math.pi)
    #print(zad3.calka2.oblicz(0.0001))
    print("Calka z 2x w przedziale [0,pi] metoda quad z scipy")
    print(integrate.quad(lambda x: 2*x, 0, math.pi)[0])
    logging.info('Stop')
