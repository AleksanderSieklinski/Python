#1 Prosze zapisać plik rozszerzenia (mod.c) oraz skrypt (setup.py). Proszę tak zmodyfikować plik rozszerzenia, aby otrzymywany wynik był poprawny, tj. np. :
# met(1,2) #3
# met(1,2,5) #8
# met(1,2,5,[2,3,4]) #17
import os

file = open("mod.c","w")
file.write("""
#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdarg.h>

static PyObject* met(PyObject* self, PyObject* args)
{
    //jezeli jednym z argumentow jest lista, to sumujemy jej elementy i dodajemy do sumy pozostale argumenty
    //jezeli nie ma listy, to sumujemy wszystkie argumenty
    int sum = 0;
    size_t n = PyTuple_Size(args);
    for(int i=0;i<n;i++)
    {
        PyObject* item = PyTuple_GetItem(args,i);
        if(PyList_Check(item))
        {
            size_t m = PyList_Size(item);
            for(int j=0;j<m;j++)
            {
                PyObject* item2 = PyList_GetItem(item,j);
                if(PyLong_Check(item2))
                {
                    sum += PyLong_AsLong(item2);
                }
            }
        }
        else if(PyLong_Check(item))
        {
            sum += PyLong_AsLong(item);
        }
    }
    return Py_BuildValue("i",sum);
}

static PyObject* insertion_sort(PyObject* self, PyObject* args)
{
    PyObject* list;
    if(!PyArg_ParseTuple(args,"O",&list))
    {
        return NULL;
    }  
    size_t n = PyList_Size(list);
    int* tab = malloc(sizeof(int)*n);
    for(int i=0;i<n;i++)
    {
        PyObject* item = PyList_GetItem(list,i);
        if(PyLong_Check(item))
        {
            tab[i] = PyLong_AsLong(item);
        }
    }
    for(int i=1;i<n;i++)
    {
        int key = tab[i];
        int j = i-1;
        while(j>=0 && key<tab[j])
        {
            tab[j+1] = tab[j];
            j--;
        }
        tab[j+1] = key;
    }
    PyObject* result = PyList_New(n);
    for(int i=0;i<n;i++)
    {
        PyList_SetItem(result,i,PyLong_FromLong(tab[i]));
    }
    free(tab);
    return result;
}

static PyObject* Euclid(int a, int b)
{
    if(b==0)
    {
        return PyLong_FromLong(a);
    }
    else
    {
        return Euclid(b,a%b);
    }
}

static PyObject* gcd(PyObject* self, PyObject* args)
{
    PyObject* dict;
    if(!PyArg_ParseTuple(args,"O",&dict))
    {
        return NULL;
    }
    PyObject* result = PyDict_New();
    PyObject* keys = PyDict_Keys(dict);
    size_t n = PyList_Size(keys);
    for(int i=0;i<n;i++)
    {
        PyObject* key = PyList_GetItem(keys,i);
        PyObject* value = PyDict_GetItem(dict,key);
        if(PyLong_Check(key) && PyLong_Check(value))
        {
            PyObject* gcd = Euclid(PyLong_AsLong(key),PyLong_AsLong(value));
            PyDict_SetItem(result,key,gcd);
        }
    }
    return result;
}

static PyMethodDef mod_methods[] = {
    {"met",met,METH_VARARGS,""},
    {"insertion_sort",insertion_sort,METH_VARARGS,""},
    {"gcd",gcd,METH_VARARGS,""},
    {NULL,NULL,0,NULL}
};

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT,
    "mod",
    "",
    -1,
    mod_methods
};

PyMODINIT_FUNC PyInit_mod(void)
{
    return PyModule_Create(&mod_module);
}
""")
file.close()

file = open("setup.py","w")
file.write("""
from distutils.core import setup, Extension

setup(name="mod",version="1.0",ext_modules=[Extension("mod",["mod.c"])])
""")
file.close()

os.system("python setup.py build")
os.system("pip3 install . --user")
import mod

print("\nZadanie 1")
print(mod.met(1,2))
print(mod.met(1,2,5))
print(mod.met(1,2,5,[2,3,4]))

#2 Proszę zaimplementować w Pythonie i w C funkcję dokonującą sortowania przez wstawianie jednowymiarowej tablicy liczb całkowitych, jako parametr do funkcji należy podać tablicę. Funkcję napisaną w C proszę wywołać z programu w Pythonie.
# Proszę porównać czasy wykonania obu funkcji dla takiej samej listy wartości losowych o rozmiarze [10,10^2,10^3,10^4] przy czym liczby losujemy z zakresu [0,rozmiar]
# Sortowanie przez wstawianie (A,n)
# for i=2 to n
#     wstawiany_element=A[i]
#     j=i-1
#     while j>0 and A[j]>wstawiany_element
#         A[j+1]=A[j]
#         j=j-1
#     A[j+1]=wstawiany_element

def insertion_sort(tab):
    for i in range(1,len(tab)):
        key = tab[i]
        j = i-1
        while j >= 0 and key < tab[j]:
            tab[j+1] = tab[j]
            j -= 1
        tab[j+1] = key
    return tab

import random
import time

print("\nZadanie 2")

print("\nJezyk Python")
for i in range(1,5):
    tab = []
    for j in range(10**i):
        tab.append(random.randint(0,10**i))
    start = time.time()
    insertion_sort(tab)
    end = time.time()
    print("Czas wykonania dla tablicy o rozmiarze 10^"+str(i)+":", end-start)

print("\nJezyk C")

for i in range(1,5):
    tab = []
    for j in range(10**i):
        tab.append(random.randint(0,10**i))
    start = time.time()
    mod.insertion_sort(tab)
    end = time.time()
    print("Czas wykonania dla tablicy o rozmiarze 10^"+str(i)+":", end-start)


#3 Proszę zmodyfikować plik rozszerzenia tak, aby była w nim funkcja, do której jako parametr będziemy przekazywać z Pythona słownik(klucze i wartości - liczby losowe z przedziału [10,100]). Dla każdej pary klucz-wartość proszę wywołać napisaną w języku C funkcję zwracającą największy wspólny
# dzielnik (poniżej) dwóch liczb przekazanych jako parametr, a wynik proszę zapisać w słowniku, który proszę zwrócić do Pythona.
# AlgorytmEuklidesa(a,b)
# if b=0
#     return a
# else
#     return AlgorytmEuklidesa(b,a mod b)
print("\nZadanie 3")
import random

dic = {}
for i in range(10):
    dic[i] = random.randint(10,100)
print(dic)

def Euclid(a,b):
    if b==0:
        return a
    else:
        return Euclid(b,a%b)

def gcd(dic):
    result = {}
    for i in range(len(dic)):
        key = list(dic.keys())[i]
        value = list(dic.values())[i]
        result[key] = Euclid(key,value)
    return result

dic = mod.gcd(dic)
print(dic)


