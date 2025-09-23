
import random

szamok = []

# 100 elemű lista feltöltése 1-99 közötti véletlenszámokkal
for i in range(100):
    rszam = random.randint(1, 100)

    # szám elhelyezése a listába 
    szamok.append(rszam)

#Ellenőrzés
print(szamok)


#kitalalandó szám beállítása
kitalalando_szam = szamok[random.randint(0, len(szamok))]

tipp = int(input("Kérek egy egész számot [1-100]: "))

if(tipp == kitalalando_szam):
    print("Gratulálok, eltaláltad a számot!")
elif(tipp < kitalalando_szam):
    print("A kitalálandó szám nagyobb!")
else:
    print("A kitalálandó szám kisebb!")

while(tipp != kitalalando_szam):
    tipp = int(input("Kérek egy egész számot [1-100]: "))
    
    if(tipp == kitalalando_szam):
        print("Gratulálok, eltaláltad a számot!")
    elif(tipp < kitalalando_szam):
        print("A kitalálandó szám nagyobb!")
    else:
        print("A kitalálandó szám kisebb!")


