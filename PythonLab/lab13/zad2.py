'''\nZad2 polega na utworzeniu klasy z dekoratorem dataclass opisujacej pracownikow i oferty pracy.\n'''
#2 Proszę utworzyć
# klasy z dekoratorem @dataclass opisujące pracowników i oferty pracy, z polami odpowiednio: nazwisko, wiek i wykształcenie oraz opis, wiek i wykształcenie (można rozszerzyć wg własnego pomysłu) (1p),
# funkcję wczytującą bazy osób i ofert, jeśli istnieją odpowiednie pliki json oraz dającą możliwość ich uzupełnienia po uruchomieniu programu, przy wczytywaniu proszę skorzystać z konstrukcji match-case (3p).
# Potrzebne będą:
# os.path.isfile(nazwa_pliku)
# json.load(plik)
# json.dump(lista_obiektów, plik, cls=EnhancedJSONEncoder), gdzie:
# class EnhancedJSONEncoder(json.JSONEncoder):
#     def default(self, o):
#         if dataclasses.is_dataclass(o):
#             return dataclasses.asdict(o)
#         return super().default(o)

# funkcję wyszukującą oferty pasujące do danej osoby/osoby pasujące do danej oferty (2p).

import json
import os.path
import dataclasses

@dataclasses.dataclass
class Pracownik:
    nazwisko: str
    wiek: int
    wyksztalcenie: str

@dataclasses.dataclass
class Oferta:
    opis: str
    wiek: list
    wyksztalcenie: str

class EnhancedJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        return super().default(o)
    
def wczytaj_pracownikow(pracownicyfile):
    if os.path.isfile(pracownicyfile):
        pracownicy = open(pracownicyfile,"r")
        return json.load(pracownicy)
        #print(json.load(pracownicy))
    if input("Czy chcesz zmienic pracownikow?") == "tak":
        lista_pracownikow = []
        while True:
            nazwisko = input("Podaj nazwisko pracownika: ")
            if nazwisko == "":
                break
            wiek = int(input("Podaj wiek pracownika: "))
            if wiek < 18:
                print("Pracownik musi byc pelnoletni")
                break
            wyksztalcenie = input("Podaj wyksztalcenie pracownika: ")
            if wyksztalcenie == "":
                print("Pracownik musi miec jakies wyksztalcenie")
                break
            pracownik = Pracownik(nazwisko,wiek,wyksztalcenie)
            lista_pracownikow.append(pracownik)
        with open(pracownicyfile,"w") as plik:
            json.dump(lista_pracownikow,plik,cls=EnhancedJSONEncoder)
        return lista_pracownikow

def wczytaj_oferty(ofertyfile):
    if os.path.isfile(ofertyfile):
        oferty = open(ofertyfile,"r")
        return json.load(oferty)
    if input("Czy chcesz zmienic oferty pracy?") == "tak":
        lista_ofert = []
        while True:
            opis = input("Podaj opis oferty: ")
            if opis == "":
                print("Nikt nie przyjmie pracy bez opisu")
                break
            wiek = int(input("Podaj wiek wymagany w ofercie: "))
            if wiek < 18:
                print("Zatrudnienie niepelnoletnich jest nielegalne")
                break
            wyksztalcenie = input("Podaj wyksztalcenie wymagane w ofercie: ")
            oferta = Oferta(opis,wiek,wyksztalcenie)
            lista_ofert.append(oferta)
        with open(ofertyfile,"w") as plik:
            json.dump(lista_ofert,plik,cls=EnhancedJSONEncoder)
        return lista_ofert

def wyszukaj_oferty(pracownicy,oferty):
    for pracownik in pracownicy:
        for oferta in oferty:
            if pracownik['wiek'] >= oferta['wiek'] and pracownik['wyksztalcenie'] == oferta['wyksztalcenie']:
                print("Oferta: ",oferta['opis']," pasuje do pracownika: ",pracownik['nazwisko'])

def wyszukaj_pracownikow(pracownicy,oferty):
    for oferta in oferty:
        for pracownik in pracownicy:
            if pracownik['wiek'] >= oferta['wiek'] and pracownik['wyksztalcenie'] == oferta['wyksztalcenie']:
                print("Pracownik: ",pracownik['nazwisko']," pasuje do oferty: ",oferta['opis'])

lista_pracownikow = wczytaj_pracownikow("pracownicy.json")
lista_ofert = wczytaj_oferty("oferty.json")
print(lista_pracownikow)
wyszukaj_oferty(lista_pracownikow,lista_ofert)
wyszukaj_pracownikow(lista_pracownikow,lista_ofert)
