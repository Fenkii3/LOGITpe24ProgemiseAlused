
# kirjuta programm mis
# küsib kasutajalt kui suur ta põrand on
# (selle jaoks on vaja ristküliku valemit kasutada, ning küsida kasutajalt a ja b külg sentimeetrites)
# küsib kasutajalt milliseid põrandaplaate ta tahab
# kasutajale antakse 6 ascii näidet, ja kasutaja sisestab numbri milline muster talle meeldib
#
# ██░░ ║┌─┐ ▀▄░░
# ░░██ ║└─┘ ░░▀▄ (muid mustreid saab välja mõelda kas tähtedest või start -> character map abiga)
# (ülejäänud kolm mustrit mõtle ise)
# väljasta kasutajale ekraan mustriga koos hinnaarvutusega.
# (esimene muster on odavaim, viimane kalleim, tehe on pindala*mustriväärtus)
# küsi kas kasutaja maksab või mitte
# kui ei maksa, alanda hinda 10% ja küsi uuesti
# kui ei maksa, alanda hinda veel samapalju ja ütle viimane hind

print("Kui suur on teie põrand?")
aKülg = int(input("Sisestage A külg: "))
bKülg = int(input("Sisestage B külg: "))
põrandaSuurus = aKülg * bKülg
print("Milliseid põrandaplaate te soovite?")

print("██░░")
print("░░██")
print("Esimene")
print("║┌─┐")
print("║└─┘")
print("Teine")
print("▀▄░░")
print("░░▀▄")
print("Kolmas")
print("░░░░")
print("████")
print("Neljas")
print("▀▄▀▄")
print("▀▄▀▄")
print("Viies")
print("┌─┐▄")
print("└─┘▀")
print("Kuues")

EsimeneVäärtus = 100
TeineVäärtus = 200
KolmasVäärtus = 300
NeljasVäärtus = 600
ViiesVäärtus = 700
KuuesVäärtus = 900

kasutajaValik = int(input("(1,2,3,4,5,6) Valige endale sobiv põrandamuster: "))
if (kasutajaValik == 1):
    print("Te valisite esimese mustri ning selle hinnaks on " + str((põrandaSuurus) * (EsimeneVäärtus)) + ".")
    kasutajaValik2 = input("Kas maksate? ")
    if kasutajaValik2 == "jah":
        print("Aitäh ostu eest!")
    elif kasutajaValik2 == "ei":
        kasutajaValik3 = input("Uus hind on" + str((põrandaSuurus) * (EsimeneVäärtus) * 90) + ", kas te maksate?")
        if kasutajaValik3 == "jah":
            print("Aitäh ostu eest!")
        elif kasutajaValik3 == "ei":
            kasutajaValik4 = input("Uus hind on" + str((põrandaSuurus) * (EsimeneVäärtus) * 80) + ", kas te maksate?")
            if kasutajavalik4 == "Jah":
                                print("Aitäh ostu eest!")
            elif kasutajaValik4 == "ei":
                                    print("Nägemist")


                                    
                                    
                    
                                           
    


