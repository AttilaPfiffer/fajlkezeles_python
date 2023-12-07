from Szemely import Szemely
szemelyek_lista = [] #itt tárolom a létrehozott osztály példányokat
fajlom = open("teszt.txt", "r", encoding = 'utf-8')
fajlom.readline()
string_lista = fajlom.readlines()
fajlom.close()
for i in range(0, len(string_lista), 1):
    """Minden sort szét kell bontani"""
    aktsor: str = string_lista[i].strip()
    print(aktsor)
    sor_lista = aktsor.split(",")
    print(sor_lista[0])
    print(sor_lista[1])
    print(sor_lista[2])
    szemely = Szemely(sor_lista[0], sor_lista[1], int(sor_lista[2]))
    szemelyek_lista.append(szemely)

for i in range(0, len(szemelyek_lista), 1):
    print(f"{szemelyek_lista[i].nev}, {szemelyek_lista[i].nem}, {szemelyek_lista[i].kor}")

import feladatok_szemelyek
atlageletkor = feladatok_szemelyek.atlageletkor(szemelyek_lista)
print(atlageletkor)

nok_szama = feladatok_szemelyek.nok(szemelyek_lista)
print(f"A nők száma: {nok_szama}")