if __name__=='__main__':
    import zad1
    print(zad1.__doc__)
    zad1
    IFS1=zad1.IFS(((0.787879, -0.424242, 1.758647, 0.242424, 0.859848, 1.408065), (-0.121212, 0.257576, -6.721654, 0.151515, 0.05303, 1.377236), (0.181818, -0.136364, 6.086107, 0.090909, 0.181818, 1.568035)), (0.90, 0.05, 0.05))
    IFS1.przeksztalcenie(10000)
    IFS1.rysowanie()
    IFS2=zad1.IFS(((0, 0.053, -7.083, -0.429, 0, 5.43), (0.143, 0, -5.619, 0, -0.053, 8.513), (0.143, 0, -5.619, 0, 0.083, 2.057), (0, 0.053, -3.952, 0.429, 0, 5.43), (0.119, 0, -2.555, 0, 0.053, 4.536), (-0.0123806, -0.0649723, -1.226, 0.423819, 0.00189797, 5.235), (0.0852291, 0.0506328, -0.421, 0.420449, 0.0156626, 4.569), (0.104432, 0.00529117, 0.976, 0.0570516, 0.0527352, 8.113), (-0.00814186, -0.0417935, 1.934, 0.423922, 0.00415972, 5.37), (0.093, 0, 0.861, 0, 0.053, 4.536), (0, 0.053, 2.447, -0.429, 0, 5.43), (0.119, 0, 3.363, 0, -0.053, 8.513), (0.119, 0, 3.363, 0, 0.053, 1.487), (0, 0.053, 3.972, 0.429, 0, 4.569), (0.123998, -0.00183957, 6.275, 0.000691208, 0.0629731, 7.716), (0, 0.053, 5.215, 0.167, 0, 6.483), (0.071, 0, 6.279, 0, 0.053, 5.298), (0, -0.053, 6.805, -0.238, 0, 3.714), (-0.121, 0, 5.941, 0, 0.053, 1.487)), (0.05, 0.05, 0.05, 0.05, 0.05, 0.05,0.05, 0.05, 0.05, 0.05, 0.05,0.05, 0.05, 0.05, 0.05, 0.05,0.05, 0.05))
    IFS2.przeksztalcenie(10000)
    IFS2.rysowanie()
    IFS3=zad1.IFS(((0.824074, 0.281428, -1.88229, -0.212346, 0.864198, -0.110607), (0.088272, 0.520988, 0.78536, -0.463889, -0.377778, 8.095795)),  (0.8, 0.2))
    IFS3.przeksztalcenie(10000)
    IFS3.rysowanie()
    import zad2
    print(zad2.__doc__)
    zad2 
    w1=zad2.Wektor3D(1, 2, 3)
    w2=zad2.Wektor3D(4, 5, 6)
    print("Wektory w1,w2")
    try: 
        if type(w1)==zad2.Wektor3D and type(w2)==zad2.Wektor3D:
            print("w1 jest wektorem")
        else:
            raise TypeError("w1 nie jest wektorem")
    except:
        print("w1 nie jest wektorem")
    print(w1)
    print(w2)
    print("Dodawanie w1,w2")
    print(w1+w2)
    print("Odejmowanie w1,w2")
    print(w1-w2)
    print("Mnozenie w1 przez 2")
    print(w1*2)
    print("Wektory w1,w2")
    print(w1)
    print(w2)
    print("Dlugosc w1")
    print(w1.dlugosc_wektora())
    print("Iloczyn skalarny w1,w2")
    print(w1.iloczyn_skalarny(w2))
    print("Iloczyn wektorowy w1,w2")
    print(w1.iloczyn_wektorowy(w2))
    print("Iloczyn mieszany w1,w2")
    print(w1.iloczyn_mieszany(w2, zad2.Wektor3D(7, 8, 9)))
    import zad3
    print(zad3.__doc__)
    zad3
    print("Strumien indukcji magnetycznej")
    print(zad3.strumien_indukcji_magnetycznej(zad2.Wektor3D(1, 2, 3), zad2.Wektor3D(4, 5, 6)))
    print("Sila Lorentza")
    print(zad3.sila_lorentza(1, zad2.Wektor3D(1, 2, 3), zad2.Wektor3D(4, 5, 6), zad2.Wektor3D(7, 8, 9)))
    print("Praca sily Lorentza")
    print(zad3.praca_sily_lorentza(1, zad2.Wektor3D(1, 2, 3), zad2.Wektor3D(4, 5, 6)))