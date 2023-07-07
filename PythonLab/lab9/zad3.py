'''\nZad3 sprawdza czy daty sa poprawne.
Jako argument przyjmuje rodzaj obchodzenia sie z bledami,
a w wyniku zwraca ValueError lub napis na ekranie (w zaleznosci od trybu),
jezeli data jest niepoprawna\n'''
#3
#Funkcję zwracającą średni wiek osób, który daty urodzenia zapisane są w plik daty.in. (3p)
#Funkcja powinna móc działać w trybie 'restrykcyjnym' - po napotkaniu niepoprawnej daty/wpisu zgłoszenie wyjątku i zakończenie działania, w trybie 'liberalnym' - niepoprawne wpisy są ignorowane.
#Linia w pliku jest poprawna, jeśli zawiera dzień, miesiąc i rok,  które tworzą poprawną datę - zgodność liczby dni w miesiącu, w tym odpowiednia długość lutego w zależności od tego czy rok jest przestępny czy nie.
#Rok przestępny: podzielny przez 4 i niepodzielny przez 100 lub podzielny przez 400.

def zad3(mode,file):
    with open(file) as f:
        lines = f.readlines()
    suma = 0
    count = 0
    for line in lines:
        line = line.split()
        if len(line) == 3:
            if int(line[1])!=2:
                if int(line[0]) <= 31 and int(line[1]) <= 12:
                    suma += int(line[2])
                    count += 1
                else:
                    if mode == "restrykcyjny":
                        raise ValueError("Niepoprawna data restrykcyjny")
                    else:
                        print("Niepoprawna data liberalny")
            elif int(line[1]) == 2 and int(line[0]) > 29:
                if mode == "restrykcyjny":
                    raise ValueError("Niepoprawna data restrykcyjny")
                else:
                    print("Niepoprawna data liberalny")
            elif int(line[0]) ==29 and int(line[1]) == 2:
                if (int(line[2]) % 4 == 0 and int(line[2]) % 100 != 0) or int(line[2]) % 400 == 0:
                    suma += int(line[2])
                    count += 1
                else:
                    if mode == "restrykcyjny":
                        raise ValueError("Niepoprawna data restrykcyjny")
                    else:
                        print("Niepoprawna data liberalny")
            elif int(line[0])<29 and int(line[1]) == 2:
                suma += int(line[2])
                count += 1
    import datetime as data
    today = data.datetime.now()
    print("Sredni wiek: " + str(today.year -suma/count))
