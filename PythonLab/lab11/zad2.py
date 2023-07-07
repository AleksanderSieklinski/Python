'''\nZad2 polega na utworzeniu iteratora liczb pseudolowych i porownanie go do wbudowanego iteratora.\n'''
#2 Proszę napisać iterator liczb pseudolosowych.
# Ciąg taki otrzymujemy ze wzoru:Xn+1 = (aXn + c) mod m, dla m = 231-1, a = 75, c = 0, x0 = 1.
# Korzystając z zaimplementowanego iteratora proszę wylosować 105 par liczb z przedziału [0,1). 
# Proszę sprawdzić jaki procent wylosowanych par mieści się w kwadracie o boku 0.1*n, gdzie n∈[1,10]. 
# Otrzymany wynik proszę porównać z wynikiem uzyskiwanym z wykorzystaniem generatora liczb pseudolosowych z języka Python (4p).

class LiczbyLosowe:
    def __init__(self,m=2**31-1,x=1,a=7**5,c=0):
        self.x=x
        self.m=m
        self.a=a
        self.c=c
    def __iter__(self):
        return self
    def __next__(self):
        self.x=(self.a*self.x+self.c)%self.m
        return self.x/self.m
    def losuj(self):
        return self.__next__()
    
        