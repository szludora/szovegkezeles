nevlista = []

# Generálj annyi véletlen számot [1, 100] között, ahány nevet bekértél. A számok az adott nevű ember korát reprezentálják. Tárold el a számokat "kor" nevezetű listában.
# Írd ki a a legidősebb ember nevét!


def fel1():
    szoveg = input("Írj valamit").upper()
    print(szoveg)

    if len(szoveg) > 10:
        print("karakterek száma:", len(szoveg))


def fel2():
    szoveg = ""

    while len(szoveg) < 3:
        szoveg = input("Adj meg legalább 3 betűs szót")


def fel4():
    szoveg = input("Írj nekem").upper()
    db = 0
    i = 0
    while i < len(szoveg):
        if szoveg[i] == "A":
            db += 1
        i += 1
    print(db, "db 'a' betű van benne")


def fel3():
    szoveg = input("Írj nekem").upper()
    i = 0

    while i < len(szoveg) and szoveg[i] != "A":
        i += 1
    if i >= len(szoveg):
        print("nincs benne a betű")
    else:
        print(f"{i + 1}. helyen van az első 'a' betű")


def fel5():
    szoveg = input("Írj").upper()
    betulista = []
    betuszam = []
    i = 0


    while i < len(szoveg):
        betu = szoveg[i]
        x = 0
        db = 0
        if betu not in betulista:
            while x < len(szoveg):
                if szoveg[x] == betu:
                    db += 1
                    if szoveg[x] not in betulista:
                        betulista.append(betu)
                x += 1
            betuszam.append(db)
        i += 1



    y = 0

    kiiras = ""

    while y < len(betulista):
        kiiras += f"{betuszam[y]} db '{betulista[y]}' betű  |   "
        y += 1
    print(kiiras)


# Írd ki a a legidősebb ember nevét!
def fel6():

    szoveg = ""

    while "@" not in szoveg:
        szoveg = input("Név?")
        if "@" not in szoveg:
            nevlista.append(szoveg.capitalize())

    print("Köszönöm, a nevek:", nevlista)


def fel7():
    import random

    i = 0
    kor = []

    while i < len(nevlista):
        vel = int(random.random()*101)+1
        kor.append(vel)
        i += 1

    print(kor)
