if __name__=='__main__':
    import logging
    import sys
    import os
    import time
    import random
    open('mod.log', 'w').close()
    logging.basicConfig(filename='mod.log', level=logging.DEBUG)
    logging.info('Start')

    os.system("rm -r build/")
    os.system("python3 setup.py build")
    sys.path.append("build/lib.linux-x86_64-3.10/")
    import mod

    import zad1
    print(zad1.__doc__)
    zad1
    try:
        
        print(mod.met(1,2))
        print(mod.met(1,2,5))
        print(mod.met(1,2,5,[2,3,4]))

    except:

        print("Nie udalo sie wykonac zadania 1")
        logging.error('Nie udalo sie wykonac zadania 1', exc_info=True)
    
    import zad2
    print(zad2.__doc__)
    zad2

    try:

        print("\nJezyk Python")

        for i in range(1,5):
            tab = []
            for j in range(10**i):
                tab.append(random.randint(0,10**i))
            start = time.time_ns()
            zad2.insertion_sort(tab)
            end = time.time_ns()
            print("Czas wykonania dla tablicy o rozmiarze 10^",i,":", end-start)


        print("\nJezyk C")

        for i in range(1,5):
            tab = []
            for j in range(10**i):
                tab.append(random.randint(0,10**i))
            start = time.time_ns()
            mod.insertion_sort(tab)
            end = time.time_ns()
            print("Czas wykonania dla tablicy o rozmiarze 10^",i,":", end-start)

    except:

        print("Nie udalo sie wykonac zadania 2")
        logging.error('Nie udalo sie wykonac zadania 2', exc_info=True)

    import zad3
    print(zad3.__doc__)
    zad3

    try:

        dic = {}
        for i in range(10):
            dic[random.randint(10,100)] = random.randint(10,100)
        print(dic)
        print("\nNajwieksze wspolne dzielniki:\n")
        print(mod.gcd(dic))
        print("\n")

    except:

        print("Nie udalo sie wykonac zadania 3")
        logging.error('Nie udalo sie wykonac zadania 3', exc_info=True)

    logging.info('Stop')
