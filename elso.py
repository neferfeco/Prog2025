
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


tipp = input("Kérek egy egész számot [1-100]: ")

while(not tipp.isdecimal()):
    print("Egész számmal játsz!")
    tipp = input("Kérek egy egész számot [1-100]: ")

tipp = int(tipp)

if(tipp < kitalalando_szam):
    print("A kitalálandó szám nagyobb!")
elif(tipp > kitalalando_szam):
    print("A kitalálandó szám kisebb!")

while(tipp != kitalalando_szam):
    tipp = input("Kérek egy egész számot [1-100]: ")
    
    while(not tipp.isdecimal()):
        print("Egész számmal játsz!")
        tipp = input("Kérek egy egész számot [1-100]: ")

    tipp = int(tipp)
    
    if(tipp < kitalalando_szam):
        print("A kitalálandó szám nagyobb!")
    elif(tipp > kitalalando_szam):
        print("A kitalálandó szám kisebb!")


print("Gratulálok, eltaláltad a számot!")







