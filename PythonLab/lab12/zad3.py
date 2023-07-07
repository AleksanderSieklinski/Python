'''\nZad3 polega na utworzeniu klasy z metodami statycznymi liczacymi obwod i pole trojkata lub czworokata.\n'''
#3 Proszę utworzyć klasę z metodami statycznymi obliczającymi obwód i pole trójkąta lub czworokąta 
# (dających się wpisać w okrąg, odpowiednio wzory Herona i Brahmagupty), 
# zdefiniowanych poprzez współrzędne wierzchołków (klasa z zadania 1) (3p)
# Wzór Herona: P=[p(p-a)(p-b)(p-c)]1/2, gdzie: a,b,c - długości boków, p - połowa obwodu
# Wzór Brahmagupty: P=[(p-a)(p-b)(p-c)(p-d)]1/2, oznaczenia j.w.
import zad1
import zad2
import math

class Figura:
    @staticmethod
    def obwod(*args):
        return sum(((args[i-1].x-args[i].x)**2+((args[i-1].y-args[i].y)**2))**0.5 for i in range(len(args)))
    @staticmethod
    def pole(*args):
        p = Figura.obwod(*args)/2
        if len(args) == 3:
            a=p-((args[0].x-args[1].x)**2+((args[0].y-args[1].y)**2))**0.5
            b=p-((args[1].x-args[2].x)**2+((args[1].y-args[2].y)**2))**0.5
            c=p-((args[2].x-args[0].x)**2+((args[2].y-args[0].y)**2))**0.5
            return (p*(a*b*c))**0.5
        elif len(args) == 4:
            a=p-((args[0].x-args[1].x)**2+((args[0].y-args[1].y)**2))**0.5
            b=p-((args[1].x-args[2].x)**2+((args[1].y-args[2].y)**2))**0.5
            c=p-((args[2].x-args[3].x)**2+((args[2].y-args[3].y)**2))**0.5
            d=p-((args[3].x-args[0].x)**2+((args[3].y-args[0].y)**2))**0.5
            return (a*b*c*d)**0.5

