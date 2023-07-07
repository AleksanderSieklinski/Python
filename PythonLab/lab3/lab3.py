# 1
import sys
import string
Str = ''.join(sys.argv[1:])
print('Nalezy dodac przynajmniej jeden argument') if len(sys.argv) == 1 else print(Str)
# 2
#Strlower = Str.lower()
#Strupper = Str.upper()
Strlower = [x for x in Str if x.islower()]
Strupper = [x for x in Str if x.isupper()]
Strnum = [x for x in Str if x.isnumeric()]
Strnlet = [x for x in Str if not x.isalpha()]
print(Strlower,'\n',Strupper,'\n',Strnum,'\n',Strnlet,end='',sep='')
# 3
Strlowerchecked = []
for x in Strlower:
    if x not in Strlowerchecked:
        Strlowerchecked.append(x)
print(Strlowerchecked)
Strlowercount = [(x,Str.count(x)) for x in Str]
print(Strlowercount)
# 4
print(sorted(Strlowercount,key= lambda i:i[1], reverse=True))
# 5
samo="aAeEiIoOuUyY"
a = sum(Str.count(i) for i in samo)
b = len(Strlower)+len(Strupper)-a
k = [(int(x),a*int(x)+b) for x in Strnum]
print(k,'\n','a =',a,'\n','b =',b,sep='')
# 6
sredniax = sum(int(x) for x in Strnum)/len(Strnum)
sredniay = sum(x[1] for x in k)/len(k)
dd = sum((i[0]-sredniax)**2 for i in k)
aa= 1/dd * sum(i[1]*(i[0]-sredniax) for i in k)
bb = sredniay - aa*sredniax
print('A = ',aa,'\n','B = ',bb,'\n','D = ',dd,'\n',end='',sep='')