'''\nZad1 polega na stworzeniu iteratora znajdujacego kolejne liczby pierwsze w zadanym zakresie.\n'''
#1 Proszę napisać iterator zwracający kolejne liczby pierwsze z zadanego zakresu dwoma sposobami i porównać ich wykorzystanie (1p).

class LiczbyPierwsze:
    def __init__(self,start,stop):
        self.start=start
        self.stop=stop
        self.liczba=start
    def __iter__(self):
        self.liczba=self.start
        return self
    def __next__(self):
        if self.liczba<self.stop:
            for i in range(2,self.liczba):
                if self.liczba%i==0:
                    self.liczba+=1
                    return self.__next__()
            self.liczba+=1
            return self.liczba-1
        raise StopIteration