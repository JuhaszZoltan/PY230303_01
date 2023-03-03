from fld03module import *

egitestek:list[Egetest] = []
file = open(file='egitestek.txt', mode='r', encoding='utf-8')

for s in file: egitestek.append(Egetest(s))
print(f'1. feladat - égitestek száma: {len(egitestek)}')

esz:int = 0
for e in egitestek:
    if e.hol_kerint == 'Nap':
        esz += 1
print(f'2. feladat - {esz} égitest kering a Nap körül')

mi:int = 0
for i in range(1, len(egitestek)):
    if egitestek[i].tavolsag < egitestek[mi].tavolsag:
        mi = i
print(f'3. feladat - {egitestek[mi].elnevezes} kering a legközelebb')