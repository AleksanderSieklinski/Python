k=[[] for i in range (10)]
k[3].extend('1,2,3') #rozdzielic i dodac
print(k)
k=[[] for i in range (10)]
k[3].append('1,2,3') #dodac 
print(k)
k=[]
for i in range(10): 
    k.append(i)
print(k)
k=list(range(10))
print(k)
k=list(range(10,0,-2))
print(k)
k=list(range(10,0,2))
print(k)
k=list([])
print(k)
k=[i for i in range(10)] # najlepiej tak pisac
print(k)
k=[8,0,17,1,10,13,19,13,10,3]
for i in k:
    i*=2
    print(i, end=', ')
print('\n',k)

for i in range (len(k)):
    k[i]*=2
    print(i, end=', ')
print('\n',k)

for i,v in enumerate(k): # v to wartosc komorki
    k[i]=1 if v>0 else -1

print('\n',k)

for i in k:
    if not i%2:
        break
else:
    print('kiedy?')

np=[1 if i>0 else -1 for i in k] # dodajemy 1 jak i>0 a jak nie to -1

N=3
k=[]
for i in range(N):
    tmp=[]
    for j in range (N):
        tmp.append((i,j))
    k.append(tmp)

k=[[(i,j) for j in range (N)] for i in range(N)]

k=[(89,34),(92,31),(96,0),(48,30),(38,10),]
c=k[:]
c.sort() #sortuje 
print(c)
c=c.sort() #c.sort zwraca None, przypisane do c, sortuje w miejscu
print(c)

c=k[:]
c.sort(key=lambda x: x[1])
print(c)

c=k[:]
c.sort(reverse=True)
print(c)

c=k[:]
for i,j in sorted(k,reverse=True):
    print(i,j)
print(c)

c=k[:]
c.reverse()
print(c)

c=k[::-1]
print(c)