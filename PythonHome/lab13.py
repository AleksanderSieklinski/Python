#1 Proszę utworzyć:
# Klasę implementującą stos, który można zainicjalizować przekazując zmienną liczbę parametrów, listę lub inny stos. Sprawdzenie typu i odpowiednią inicjalizację proszę wykonać korzystając z konstrukcji match/case. W klasie proszę zdefiniować metodę pozwalającą na dodanie
# elementu do stosu oraz metodę pozwalającą na jego wypisanie. Proszę przetestować działanie klasy.
# Klasę implementującą stos posortowany, dziedziczącą po wcześniej zdefiniowanej klasie. Inicjalizacja jak wcześniej oraz posortowanym stosem, przy czym przed sortowaniem proszę zachować elementy typu najliczniej reprezentowanego.
# W klasie proszę zdefiniować metodę pozwalającą na dodanie elementu pod warunkiem, że zachowa to porządek sortowania.
# Proszę sprawdzić jaki jest średni rozmiar posortowanego stosu, który wypełniamy całkowitymi liczbami losowymi z przedziału [0,100] losując 100 wartości (średnia po 100 powtórzeniach).
print("Zadanie 1")

import random

class Stack:
    def __init__(self, *args):
        self.stack = []
        for arg in args:
            self.stack.append(arg)
    def push(self, value):
        self.stack.append(value)
    def print(self):
        print(self.stack)

class SortedStack(Stack):
    def __init__(self, *args):
        super().__init__(*args)
        self.stack.sort()
    def push(self, value):
        if value >= self.stack[-1]:
            self.stack.append(value)
        else:
            print("Nie mozna dodac elementu do posortowanego stosu")
    def print(self):
        print(self.stack)

Stack1 = Stack(1,2,3,4,5)
Stack1.print()
Stack1.push(6)
Stack1.print()
Stack2 = SortedStack(1,2,3,4,5)
Stack2.print()
Stack2.push(6)
Stack2.print()
Stack2.push(3)
Stack2.print()
Stack3=SortedStack(random.randint(0,100))
for i in range(100):
    Stack3.push(random.randint(0,100))
print("Dlugosc stosu: ", end="")
print(len(Stack3.stack))
#2 Proszę utworzyć:
# klasy opisujące pracowników i oferty pracy, z polami odpowiednio: nazwisko, wiek i wykształcenie oraz opis, wiek i wykształcenie (można rozszerzyć wg własnego pomysłu)
# funkcję wczytującą bazy osób i ofert, jeśli istnieją odpowiednie pliki json oraz dającą możliwość ich uzupełnienia po uruchomieniu programu, przy wczytywaniu proszę skorzystać z funkcji match-case
# Potrzebne będą:
# os.path.isfile(nazwa_pliku)
# json.load(plik)
# json.dump(lista obiektów, plik, cls=EnhancedJSONEncoder) gdzie:
# class EnhancedJSONEncoder(json.JSONEncoder):
#     def default(self, o):
#         if dataclasses.is_dataclass(o):
#             return dataclasses.asdict(o)
#         return super().default(o)
# funkcję wyszukującą oferty pasujące do danej osoby/osoby pasujące do danej oferty
print("Zadanie 2")

import json
import os.path
import dataclasses

@dataclasses.dataclass
class Person:
    name: str
    age: int
    education: str

@dataclasses.dataclass
class JobOffer:
    description: str
    age: int
    education: str

class EnhancedJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        return super().default(o)
    
def load_data():
    if os.path.isfile("people.json"):
        with open("people.json", "r") as file:
            people = json.load(file)
    else:
        people = []
    if os.path.isfile("job_offers.json"):
        with open("job_offers.json", "r") as file:
            job_offers = json.load(file)
    else:
        job_offers = []
    return people, job_offers

def save_data(people, job_offers):
    with open("people.json", "w") as file:
        json.dump(people, file, cls=EnhancedJSONEncoder)
    with open("job_offers.json", "w") as file:
        json.dump(job_offers, file, cls=EnhancedJSONEncoder)

def add_person(people):
    name = input("Podaj nazwisko: ")
    age = int(input("Podaj wiek: "))
    education = input("Podaj wyksztalcenie: ")
    people.append(Person(name, age, education))

def add_job_offer(job_offers):
    description = input("Podaj opis: ")
    age = int(input("Podaj wiek: "))
    education = input("Podaj wyksztalcenie: ")
    job_offers.append(JobOffer(description, age, education))

def find_job_offers(people, job_offers):
    for person in people:
        print("Osoba: ", end="")
        print(person)
        for job_offer in job_offers:
            if person.age >= job_offer.age and person.education == job_offer.education:
                print("Oferta: ", end="")
                print(job_offer)

def find_people(people, job_offers):
    for job_offer in job_offers:
        print("Oferta: ", end="")
        print(job_offer)
        for person in people:
            if person.age >= job_offer.age and person.education == job_offer.education:
                print("Osoba: ", end="")
                print(person)

people, job_offers = load_data()
while True:
    print("1. Dodaj osobe")
    print("2. Dodaj oferte pracy")
    print("3. Wyszukaj oferty pracy dla osob")
    print("4. Wyszukaj osoby dla ofert pracy")
    print("5. Wyjdz")
    choice = int(input("Wybierz opcje: "))
    if choice == 1:
        add_person(people)
    elif choice == 2:
        add_job_offer(job_offers)
    elif choice == 3:
        find_job_offers(people, job_offers)
    elif choice == 4:
        find_people(people, job_offers)
    elif choice == 5:
        break
    else:
        print("Niepoprawny wybor")
save_data(people, job_offers)