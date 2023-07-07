'''\nZad2 polega na sprawdzeniu czasu wykonania insertion sort miedzy Pythonem a jezykiem C, gdie funkcje C importujemy z gotowego pliku.\n'''
#2 Proszę zaimplementować w Pythonie i w C funkcję dokonującą sortowania przez wstawianie jednowymiarowej tablicy liczb całkowitych, jako parametr do funkcji należy podać tablicę. 
# Funkcję napisaną w C proszę wywołać z programu w Pythonie. 
# Proszę porównać czasy wykonania obu funkcji dla takiej samej listy wartości losowych o rozmiarze  [10, 102, 103, 104] przy czym liczby losujemy z zakresu [0, rozmiar] (4p)
# Sortowanie przez wstawianie (A, n)
# 1.  for i=2 to n :
# 2       # Wstaw A[i] w posortowany ciąg A[1 ... i-1]
# 3.      wstawiany_element = A[i]
# 4.      j = i - 1
# 5.      while j>0 and A[j]>wstawiany_element:
# 6.          A[j + 1] = A[j]
# 7.          j = j - 1
# 8.      A[j + 1] = wstawiany_element

# import os
# import random
# import time

# os.system("python3 setup.py build")
# import mod

def insertion_sort(tab):
    for i in range(1,len(tab)):
        key = tab[i]
        j = i-1
        while j >= 0 and key < tab[j]:
            tab[j+1] = tab[j]
            j -= 1
        tab[j+1] = key
    return tab