#1 Proszę napisać funkcję, która pozwoli na wypisanie: n początkowych wierszy pliku, n końcowych wierszy pliku,
# co n-tego wiersza pliku, n-tego słowa ze wszystkich wierszy i n-tego znaku ze wszystkich wierszy. Nazwę pliku oraz n przekazujemy jako parametr do funkcji. Każdy podpunkt==jedna linia kodu (1.5p)
print("Zadanie 1")
# wszystko ma byc w jednej funkcji
def func(filename,n):
    with open(filename) as f:
        line = f.readlines()
        print("n początkowych wierszy pliku")
        print(line[:n])
        print("n końcowych wierszy pliku")
        print(line[-n:])
        print("co n-tego wiersza pliku")
        print(line[::n])
        print("n-tego słowa ze wszystkich wierszy")
        print([i.split()[n] for i in line if n<len(i.split())])
        print("n-tego znaku ze wszystkich wierszy")
        print([i[n] for i in line if n<len(i)])
filename = "lab8.py"
func(filename,3)

#2 Odczytujemy wartości ze wszystkich plików, których nazwy rozpoczynają się od data i kończą na in w katalogu bieżącym. Na wyjściu proszę utworzyć jeden plik z trzema kolumnami:
# pierwsza kolumna - numer wiersza,
# druga kolumna - uśredniona wartość z danego wiersza ze wszystkich plików (numpy.average),
# trzecia kolumna - odchylenie standardowe wartości z danego wiersza ze wszystkich plików (numpy.std)
print("Zadanie 2")

from numpy import mean, std, average
import glob

def read_data():
    files = [i for i in glob.glob("data*in")]
    data = {}
    for i in files:
        with open(i) as f:
            for x,y in enumerate(f):
                data.setdefault(x,[]).append(float(y))
    return data


def write_data(data):
    f = open("res2.out", "w")
    for i in range(len(data)):
        f.write(str(i) + " ")
        f.write(str(average(data[i])) + " ")
        f.write(str(std(data[i])) + "\n")

data = read_data()
write_data(data)


#3 Proszę napisać funkcję, tworzącą plik z instrukcjami pozwalającymi na wygenerowanie wykresu plików j.w. + wynikowego (łącznie z odchyleniem standardowym)*patrz niżej, proszę skorzystać z potrójnego cudzysłowa
print("Zadanie 3")

import matplotlib.pyplot as plt

def draw():
    with open("res2.out") as f:
        data = f.readlines()
    x = [float(i.split()[1]) for i in data]
    y = [float(i.split()[2]) for i in data]
    plt.plot(x, y, 'ro')
    plt.xlabel('average')
    plt.ylabel('std')
    plt.savefig("res3.png")

draw()
plt.clf()
#4 Pliki o nazwach rok.in (rank.zip) zawierają informację o pozycji na liście rankingowej pewnych osób, w kolejnych latach.
# Proszę utworzyć zbiorczy plik, w którym w pierwszej kolumnie znajdzie się "nazwisko",
# kolejne kolumny będą odpowiadały pozycji danej osoby na liście rankingowej w kolejnych latach, od 2000 do 2020 (2.5p)
print("Zadanie 4")

def readfiles():
    files = glob.glob("20*.txt")
    data = []
    for file in files:
        data.append([line.split() for line in open(file).readlines()])
    return data

def writefile(data):
    f = open("res4.out", "w")
    f.write("Nazwisko")
    g=sorted(glob.glob("20*.txt"))
    for file in g:
        f.write(" " + file[:4])
    f.write("\n")
    sl={}
    for i in range(len(data)):
        for j in range(len(data[i])):
            sl.setdefault(data[i][j][0],{}).setdefault(g[i][:4],data[i][j][1])
    for i in sl:
        f.write(i)
        for j in g:
            if j.split('.')[0] in sl[i]:
                f.write("    " + sl[i][j[:4]])
            else:
                f.write("    -")
        f.write("\n")
data = readfiles()
writefile(data)

#5 Proszę sporządzić histogram słów rozpoczynających się na daną literę alfabetu (dla całego alfabetu) ze wszystkich plików pasujących do określonego wzorca w katalogu bieżącym,
# opcje wyświetlenia: sortowanie alfabetyczne, bądź po liczbie słów (2.5p)
print("Zadanie 5")
import numpy as np

files = glob.glob("zad*.in")
data = []
for file in files:
    data.append([line.split() for line in open(file).readlines()])
n=1
x = [chr(i) for i in range(97, 123)]
y = []
for i in range(len(x)):
    y.append(0)
    for j in range(len(data)):
        for k in range(len(data[j][0])):
            if data[j][0][k][0].lower() == x[i]:
                y[i] += 1
if n==1: #sortowanie alfabetyczne
    for i in range(len(x)):
        for j in range(i+1, len(x)):
            if y[i] < y[j]:
                y[i], y[j] = y[j], y[i]
                x[i], x[j] = x[j], x[i]
plt.bar(x, y)
plt.xlabel("Litera alfabetu")
plt.ylabel("Liczba wystąpień")
plt.savefig("res.pdf")
