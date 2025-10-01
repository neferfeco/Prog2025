

try:
    with open("F1-2024dec1.csv", encoding="utf-8") as fajl:
        f = fajl.read()
        
        n = 4 / 0
        
        print(f)
        print(n)

except Exception as ex:
    print(f"Halihóóóóó!: Hiba oka: {ex}")
except FileNotFoundError:
    print("Hiba a fájl megnyitása közben!")
except ZeroDivisionError:
    print("Ne ossz 0-val!")




print("ITT A PROGRAM VÉGE!")

