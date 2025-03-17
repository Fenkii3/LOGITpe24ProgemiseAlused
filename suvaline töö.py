# kirjuta programm mis
# küsib kasutajalt tsükli abil tema nime, tsükkel ei tohi katkeda:
# - kui kasutaja ei sisesta midagi
# - kui kasutaja sisestab rohkem kui 25 tähte
# - - siis öeldakse ka kasutajale, et 25 tähte on maksimaalne nime pikkus
# küsib kasutajalt tsüklis tema saadetise pikkust, laiust, kõrgust ja raskust. tsükkel ei tohi katkeda:
# - kui kasutaja paneb vastusteks 0
# - kui kasutaja paneb vastusteks mitte midagi
# küsib kasutajalt sihtriiki, tsükkel ei tohi katkeda:
# - kui kasutaja ei sisesta midagi
# - kui kasutaja sisestab rohkem kui 25 tähte
# Arvutab kasutaja saadetise ruumala.
# Arvutab kasutajale saadetise maksumuse. (ruumala * raskus)
# Küsib kasutajalt tsükli abil kas ta maksab, tsükkel ei tohi katkeda:
# - kui kasutaja ei sisesta midagi
# - kui kasutaja sisestab midagi muud kui jah/ei
# - - Kui kasutaja on ei öelnud rohkem kui 5 korda, muutub kasutajale esitatav küsimus ähvardavamaks
# - kui kasutaja ütleb jah, siis öeldakse kasutajale et "<nimi>, teie saadetis on teel <sihtriik>i"
 
# kasuta while tsüklit

name = ""
while((name == "") or (len(name) < 1) or (name == " ")):
    if len(name) > 25:
        print("nimi on liiiiiiiiiigaaaaa pikkkk")
    name = input("Palun sisesta oma nimi: ")
print(name)

pikkus = 0
while((pikkus == 0)):
    print("Palun sisestage saadetise pikkus")
    pikkus = int(input())

laius = 0
while((laius == 0)):
    print("Palun sisestage saadetise laius")
    laius = int(input())

kõrgus = 0
while((kõrgus == 0)):
    print("Palun sisestage saadetise kõrgus")
    kõrgus = int(input())

raskus = 0
while((raskus == 0)):
    print("Palun sisestage saadetise raskus")
    raskus = int(input())
    
sihtriik = ""
while((sihtriik == "") or (len(sihtriik) > 25) or (sihtriik == " ")):
    if len(sihtriik) > 25:
        print("Riigi nimi on liiga pikk, 25 tähte on max pikkus")
    sihtriik = input("Palun sisesta sihtriik: ")
    
kasMaksab = ""
mituKordaKüsitudOn = 0
positiivneVastus = False
while( (kasMaksab == "") or (kasMaksab.lower() != "jah") or (kasMaksab.lower() != "ei") or (kasMaksab.lower() == "ei")) and (positiivneVastus == False):
    mituKordaKüsitudOn += 1
    if (kasMaksab.lower() == "jah"):
        positiivneVastus = True
        print(name+", teie saadetis on teel "+sihtriik)
    else:
        if (mituKordaKüsitudOn > 5):
            kasMaksab = input("Olete kindel, et soovite külma arvet teha, rsk= (jah/ei): ")
        else:
            kasMaksab = input("Kas soovite maksta? (jah/ei): ")



    
