'''\nZad1 sprawdza poprawnosc numeru karty kredytowej.
Jako dane wejsciowe przyjmuje numer karty, w razie bledu zwraca ValueError,
a w razie powodzenia zwraca napis ze numer jest poprawny\n'''
#1
#Funkcję sprawdzającą poprawność numeru karty kredytowej (2p)
#Algorytm Luhna - cyfry w numerze karty indeksujemy od 15 (skrajna lewa) do 0 (skrajna prawa), indeksom parzystym nadajemy wagę jeden, a nieparzystym dwa,
#przy czym wartości na nieparzystych indeksach podwajamy, jeśli otrzymana liczba jest większa od 10 sumujemy jej cyfry. W numerze karty zastępujemy odpowiednio cyfry i przemnażamy je przez wagi,
#a następnie sumujemy. Jeżeli otrzymana wartość jest podzielna bez reszty przez 10 uznajemy numer karty za poprawny.
#Wyjątek zgłaszamy w przypadku kiedy parametr przekazany do funkcji nie składa się z samych cyfr, ma niepoprawną długość lub otrzymana suma kontrolna jest niepoprawna.
#Przykłady do testów : 924803-zla, 1234567898765437-ok, 1234567891234564-zla, 1234567891234563-ok

def zad1(numer):
    if len(numer)!=16:
        raise ValueError("Zly format")
    elif numer.isdigit() == False:
        raise ValueError("Zly format")
    else:
        suma = 0
        arr={}
        for i in range(15,-1,-1):
            if i%2 == 0:
                arr[i] = int(numer[15-i])
            else:
                arr[i] = int(numer[15-i])*2
                if arr[i] > 9:
                    strarr = str(arr[i])
                    arr[i] = int(strarr[0]) + int(strarr[1])
        for i in range(0,16):
            suma += arr[i]
        if suma%10 != 0:
            raise ValueError("Zly format")
        else:
            print("Poprawny format")
