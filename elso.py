
import random

szamok = []

# 100 elemű lista feltöltése 1-99 közötti véletlendzámokkal
for i in range(100):
    #.... szám generálás
    rszam = random.randint(1, 100)

    # szám elhelyezése a listába 
    szamok.append(rszam)

#Ellenőrzés
print(szamok)



#egyszámjáték
jatek_szam = 0
nem_talaltDB = 0

#kitalalandó szám beállítása
kitalalando_szam=input()
