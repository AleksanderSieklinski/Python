'''\nzadanie 2 polega na stworzeniu klasy Wektor3D, ktory jest Wektorem o trzech wspolrzednych,
z przeciazonymi operatorami dodawania, odejmowania, mnozenia, dzielenia oraz mnozen wektorow\n'''
#2 Proszę utworzyć klasę Wektor 3D, którego stan początkowy jest określony przez metodę inicjalizacyjna. W klasie proszę zdefiniować metody przeciążające operatory 
# dodawania, odejmowania, mnożenia (mnożenie wektora przez liczbę) oraz metodę str. 
# Proszę napisać także metody zwracające odpowiednio długość wektora, iloczyn skalarny, wektorowy i mieszany (4p).

import math

class Wektor3D:
    def __init__(self, x, y, z):
        self.x=x
        self.y=y
        self.z=z
    def __add__(self, other):
        return Wektor3D(self.x+other.x, self.y+other.y, self.z+other.z)
    def __sub__(self, other):
        return Wektor3D(self.x-other.x, self.y-other.y, self.z-other.z)
    def __mul__(self, other):
        return Wektor3D(self.x*other, self.y*other, self.z*other)
    def __str__(self):
        return f'({self.x}, {self.y}, {self.z})'
    def dlugosc_wektora(self):
        return (self.x**2+self.y**2+self.z**2)**(1/2)
    def iloczyn_skalarny(self, other):
        return self.x*other.x+self.y*other.y+self.z*other.z
    def iloczyn_wektorowy(self, other):
        return Wektor3D(self.y*other.z-self.z*other.y, self.z*other.x-self.x*other.z, self.x*other.y-self.y*other.x)
    def iloczyn_mieszany(self, other, other2):
        return self.iloczyn_skalarny(other.iloczyn_wektorowy(other2))