
verseny_adatok = []

try:
    with open("F1-2024dec.csv", encoding="utf-8") as fajl:
        verseny_adatok = fajl.readlines()

except Exception as ex:
    print(f"Halihóóóóó!: Hiba oka: {ex}")
except FileNotFoundError:
    print("Hiba a fájl megnyitása közben!")


    """
    1. [X] Megszámolás
    2. [X] Eldöntés 1
       [X] Eldöntés 2
    3. [X] Kiválasztás
    4. [X] Keresés
    5. [] Sorozatszámítás, összegzés
    6. [] Minimum/maximum kiválasztás
    
    7. [] Másolás
    8. [] Kiválogatás
    9. [] Szétválogatás
    10.[] Metszet
    11.[] Únió
    
    12. Rendezés
        [] Egyszerű cserés rendezés
        [] Buborékos
        [] Minimum kiválasztásos
    """


# -----------------------------------------------

# 1. Hány versenyző nem szerzett még pontot?
db = 0

for i in range(1, len(verseny_adatok)):
    if(int(verseny_adatok[i].split(',')[1]) == 0):
        db = db + 1

print(f"{db} versenyző nem szerzett még pontot.\n")


# 2.A Van-e Fernando nevű versenyző?

i = 0
while (i<len(verseny_adatok)and "Fernando" not in verseny_adatok[i]):
    i=i+1
if (i<len(verseny_adatok)):
    print("Van ilyen versenyző")
else:
    print("Nincs ilyen versenyző")  


# 2.B Mindenki szerzett már 90 pontot?

i=1
while i<len(verseny_adatok) and int(verseny_adatok[i].split(",")[1])>=90:
    i=i+1
if i==len(verseny_adatok):
    print("van")
else:
    print("nem")
    
3. #Melyik istálló pilotája a Yuki Tsunoda?
i=0
while verseny_adatok[i].split(",")[0]!="Yuki Tsunoda":
    i+=1
print("Yuki Tsunoda a",verseny_adatok[i].split(",")[2])

#melyik csapatban volt Pierre Gasly?
i=1
while i<len(verseny_adatok) and "Pierre Gasly" not in verseny_adatok[i]:
    i=i+1
if i<len(verseny_adatok):
    print("Pierre Gasly", verseny_adatok[i].split(",")[2].strip(), "csapatban van!:)")
else:
    print("Nincs ilyen versenyző ezért egyik csapatban sincs bennt!:(")















print("ITT A PROGRAM VÉGE!")

