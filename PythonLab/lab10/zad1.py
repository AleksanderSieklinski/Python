'''\nzadanie 1 polega na stworzeniu klasy ifs rysujacej otrzymane wspolczynniki w zaleznosci od przypisanego dla nich prawdopodobienstwa\n'''
#1 Proszę utworzyć klasę IFS (Iterated Function System), a w niej (5p).:
#metodę inicjalizującą przyjmującą jako parametr współczynniki przekształcenia oraz prawdopodobieństwa i określającą początkowe współrzędne punktu jako (0,0),
#metodę dokonującą przekształcenia; jako parametr proszę przekazać liczbę iteracji. W każdej iteracji przy obliczaniu nowych współrzędnych punktu należy wylosować z określonym prawdopodobieństwem inną szóstkę z danego zestawu współczynników.
#Współrzędne obliczamy wg wzorów:
#x(t+1)=a*x(t)+b*y(t)+c
#y(t+1)=d*x(t)+e*y(t)+f
#metodę rysującą otrzymany wynik
#Przykładowe zestawy współczynników wraz z prawdopodobieństwem:
#((0.787879, -0.424242, 1.758647, 0.242424, 0.859848, 1.408065), (-0.121212, 0.257576, -6.721654, 0.151515, 0.05303, 1.377236), (0.181818, -0.136364, 6.086107, 0.090909, 0.181818, 1.568035)), (0.90, 0.05, 0.05)
#((0, 0.053, -7.083, -0.429, 0, 5.43), (0.143, 0, -5.619, 0, -0.053, 8.513), (0.143, 0, -5.619, 0, 0.083, 2.057), (0, 0.053, -3.952, 0.429, 0, 5.43), (0.119, 0, -2.555, 0, 0.053, 4.536), (-0.0123806, -0.0649723, -1.226, 0.423819, 0.00189797, 5.235), (0.0852291, 0.0506328, -0.421, 0.420449, 0.0156626, 4.569), (0.104432, 0.00529117, 0.976, 0.0570516, 0.0527352, 8.113), (-0.00814186, -0.0417935, 1.934, 0.423922, 0.00415972, 5.37), (0.093, 0, 0.861, 0, 0.053, 4.536), (0, 0.053, 2.447, -0.429, 0, 5.43), (0.119, 0, 3.363, 0, -0.053, 8.513), (0.119, 0, 3.363, 0, 0.053, 1.487), (0, 0.053, 3.972, 0.429, 0, 4.569), (0.123998, -0.00183957, 6.275, 0.000691208, 0.0629731, 7.716), (0, 0.053, 5.215, 0.167, 0, 6.483), (0.071, 0, 6.279, 0, 0.053, 5.298), (0, -0.053, 6.805, -0.238, 0, 3.714), (-0.121, 0, 5.941, 0, 0.053, 1.487)), prawdopodobieństwo jednakowe
#((0.824074, 0.281428, -1.88229, -0.212346, 0.864198, -0.110607), (0.088272, 0.520988, 0.78536, -0.463889, -0.377778, 8.095795)),  (0.8, 0.2)

import random
import matplotlib.pyplot as plt

class IFS:
    def __init__(self, wspolczynniki, prawdopodobienstwo):
        self.x=0
        self.y=0
        self.wspolczynniki=wspolczynniki
        if (len(wspolczynniki)!=len(prawdopodobienstwo)):
            prawdopodobienstwo=[1/len(wspolczynniki) for i in range(len(wspolczynniki))]
        self.prawdopodobienstwo=prawdopodobienstwo
        self.x_list=[]
        self.y_list=[]

    def przeksztalcenie(self, iteracje):
        for i in range(iteracje):
            losowanie=random.choices(self.wspolczynniki, self.prawdopodobienstwo)[0]
            a,b,c,d,e,f=losowanie[0],losowanie[1],losowanie[2],losowanie[3],losowanie[4],losowanie[5]
            self.x,self.y=(a*self.x)+(b*self.y)+c,(d*self.x)+(e*self.y)+f
            self.x_list.append(self.x)
            self.y_list.append(self.y)

    def rysowanie(self):
        plt.plot(self.x_list, self.y_list, 'o', color='pink')
        #colors = ['pink', 'red', 'green', 'blue', 'yellow', 'black', 'orange', 'purple', 'brown', 'gray']
        #for i in range(len(self.x_list)):
            #plt.plot(self.x_list[i], self.y_list[i], 'o', color=colors[i%len(colors)])
        plt.show()

