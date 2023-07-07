#1
k = [1,3,5,5,6,5,3,2,8,9]
print('Zad1 ')
print(k)
x=5
for i in range (k.count(x)):
    k.remove(x)
print(k)

#for el in k[:]:
#    if el==x:
#        k.remove(x)
#2
k = [1,3,5,6,5,3,2,8,9]
print('Zad2 ')
print(k)
x=5
while x in k:
    k.remove(x)
print(k)
#3
k = [1,3,5,6,5,3,2,8,9]
print('Zad3 ')
for i in range(0,len(k),2):
    print(k[i])
#4
k = [1,3,5,6,5,3,2,8,9]
print('Zad4 ')
j=[i for i in k[0::2]]
print(j)
    
#5
k = [1,3,5,6,5,3,2,8,9]
print('Zad5 ')
for i in range(-len(k),0,2):
    print(k[i])
#6
k = [1,3,5,6,5,3,2,8,9]
print('Zad6 ')
print(k[-1::-2]) #[-1:0:-2] nie wypisuje ostatniego
#petla for
#7
print('Zad7 ')
k=[(i,k[i]) for i in range(len(k))]
print(k)
#8
print('Zad8 ')
k.sort(key = lambda x:x[1])
print(k)
#9
print('Zad9 ')
k = [1,3,5,6,5,3,2,8,9]
k=[(i,x) for i,x in enumerate(k) if x%2==0]
print(k)
#10
print('Zad10 ')
k = [1,3,5,6,5,3,2,8,9]
k=[(i,x) if i>x else (x,i) for i,x in enumerate(k)]
print(k)
#11.1
print('Zad11.1 ')
N=4
k=[[0]*N for i in range(N)]
for i in range(N):
    for j in range(N):
        k[i][j]=1 if i>0 and i<3 and j>0 and j<3 else 0
        print(k[i][j],end=' ')
    print()
#11.2
print('Zad11.2 ')
N=4
k=[[0]*N for i in range(N)]
for i in range(N):
    for j in range(N):
        k[i][j]=1 if i==j else 0
        print(k[i][j],end=' ')
    print()
#11.3
print('Zad11.3 ')
N=4
k=[[0]*N for i in range(N)]
for i in range(N):
    for j in range(N):
        k[i][j]=1 if N-j-i==1 else 0
        print(k[i][j],end=' ')
    print()
#11.4
print('Zad11.4 ')
N=4
k=[[0]*N for i in range(N)]
for i in range(N):
    for j in range(N):
        k[i][j]=1 if N-j-i==1 else 0
        if i==j:
             k[i][j]=1
        print(k[i][j],end=' ')
    print()
#11.5
print('Zad11.5 ')
N=4
k=[[0]*N for i in range(N)]
for i in range(N):
    for j in range(N):
        
        if i%2==0 and j%2 or i%2==1 and j%2==0:
             k[i][j]=1
        print(k[i][j],end=' ')
    print()