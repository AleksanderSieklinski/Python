'''\nZad3 polega na znalezieniu najwiekszych wspolnych dzielnikow dla elementow slownika (klucz i wartosc).\n'''
#3 Proszę zmodyfikować plik rozszerzenia tak, aby była w nim funkcja, do której jako parametr będziemy przekazywać z Pythona słownik 
# (klucze i wartości - liczby losowe z przedziału [10,100]). Dla każdej pary (klucz,wartość) proszę wywołać napisaną w języku C 
# funkcję zwracającą największy wspólny dzielnik (poniżej) dwóch liczb przekazanych jako parametr, a wynik proszę zapisać w słowniku, 
# który proszę zwrócić do Pythona (4p).

# AlgorytmEuklidesa(a, b)
# 1: if b = 0 then
# 2: return a
# 3: else
# 4: return AlgorytmEuklidesa(b, a mod b)
# 5: end if 

#import os
#import random
#os.system("rm -r build/")
#os.system("python3 setup.py build")
#import sys
#sys.path.append("build/lib.linux-x86_64-3.10/")
#import mod

#dic = {}
#for i in range(10):
#    dic[random.randint(10,100)] = random.randint(10,100)
#print(dic)

#print(mod.gcd(dic))
