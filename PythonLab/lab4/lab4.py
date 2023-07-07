import random
import string
#1 Proszę utworzyć k-elementową listę całkowitych wartości losowych z przedziału [0,5k).
#  Proszę sprawdzić ile elementów pozostaje na swoim miejscu po losowym przemieszaniu listy, mieszanie proszę wykonać 100 razy a wyniki zapisywać w słowniku (2p)
k=5
l=[random.randint(1,5*k) for i in range(k)]

print(l)
l1=l.copy()
s=dict.fromkeys(range(k+1),0)
for i in range(100):
    random.shuffle(l1)
    temp=sum(1 for j in range(k) if l[j]!=l1[j])
    s[temp]+=1
print(s)
#2 Proszę utworzyć losowy string o długości k zawierający tylko małe litery, pomiędzy poszczególne litery proszę wstawić kropkę (1p)
stri=[random.choice(string.ascii_lowercase) for i in range(k)]
str='.'.join(stri)
print(stri)
print(str)
#3 Proszę utworzyć listę stu całkowitych wartości losowych z przedziału [0,20). Następnie na jej podstawie proszę utworzyć słownik, w którym klucze są liczbami z listy, a wartościami lista ich indeksów.
#  a)w rozwiązaniu proszę wykorzystać metodę setdefault i funkcjię enumerate (1p)
list=[random.randint(0,19) for i in range(100)]
s={}
for i,x in enumerate(list):
    s.setdefault(x,[]).append(i)
print(s)
#  b)w rozwiązaniu proszę wykorzystać metody setdefault i index, i nie korzystać ani z range, ani z enumerate (1.5p)
s={}
for x in list:
    s.setdefault(x,[]).append(list.index(x,s[x][-1]+1 if s[x] else 0))
print(s)
#4 Proszę sprawdzić ile spośród 1000 losowych wartości całkowitych składających się z n cyfr, gdzie n jest z przedziału [3,6], jest liczbami palindromowymi. Wynik proszę zapisać w słowniku - jedna linijka (2.5p)
s={k: f'{random.randint(100,999999,1)}' for k in range(1000)}
#5 Proszę utworzyć dwa słowniki o rozmiarze 10, w których kluczami są kolejne liczby naturalne, a wartościami liczby losowe z przedziału [1,100). Następnie w obu słownikach proszę zamienić miejscami klucze z wartościami.
# Na podstawie tak otrzymanych słowników proszę utworzyć nowy słownik, w którym klucze są kluczami występującymi jednocześnie w obu wcześniej utworzonych słownikach, wartościami natomiast są dwuelementowe krotki wartości związanych z danym kluczem w słownikach oryginalnych  (2p)
s={i: random.randrange(1,100) for i in range(10)}
s1={i: random.randrange(1,100) for i in range(10)}
s={x: i for i,x in s.items()}
s1={x: i for i,x in s1.items()}
print('\n',s,'\n',s1)
s2={}
for i,x in s.items():
    for j,y in s1.items():
        if i==j:
            s2={i: (x,y)}
print(s2)