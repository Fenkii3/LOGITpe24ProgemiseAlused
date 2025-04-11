kNimi = "" #muutuja mis hoiab kasutaja ees ja perekonnanime, hetkel tühi
while (kNimi == ""): #tsükkel kasutajanime küsimiseks, toimib niikaua kuni muutuja jääb tühjaks
       kNimi = input("Sisesta oma ees-ja perekonnanimi").title() #küsitakse kasutajalt sisendiks tema nimi, .title() töötleb nime Esi Suur Tähe kujule kõikides sõnades
kasOnLoom = "" #muutuja mis hoiab vastust kas kasutajal on loom, hetkel tühi
millineLoomaliik = "" #muutuja mis hoiab kasutaja loomaliiki, hetkel tühi
while (millineLoomaliik == ""): #tsükkel mis toimib niikaua kuni loomaliik on sisestatud
    kasOnLoom = input("Kas sul on koduloom?").lower() #küsime kasutajalt sõnega kas tal on koduloom
    if kasOnLoom == "jah": #tingimuslause mis kontrollib kasutaja vastust (kas tal on loom või mitte)
        millineLoomaliik = input("Kas sul on koduloomaks koer või kass?").lower() #juhul kui tal on, küsime kasutajalt loomaliiki
    else: #kõikidel muudel juhtudel
        break #tsükkel katkestatakse
    
if(kasOnLoom == "jah"): #tingimuslause mis kontrollib kasutaja vastust (kas tal on loom või
    if(millineLoomaliik == "kass"): #kui loomaliigiks on kass
        mituKassi = int(input("Mitu kassi sul on?")) #küsime mitu kassi tal on
        kassiNimed = "" #muutuja mis hoiab kasside nimesid
        mitmes = 0 #teksti kuvamiseks vajalik muutuja, mis kuvab küsimise järjekorranumbrit
        
        while (mituKassi > 0): #tsükkel, mis toimib niikaua, kuni kõikide kasside nimed on teada saadud.
            print("Sisesta "+str(mitmes)+" kassi nimi:") #kuvame kasutajale küsimuse kassi nime sisestuse kohta. kasutatakse järjekorranumbri muutujat
            kassiNimed+=", " #kassi nimede muutujasse, liidetakse juurde eralduskoht milleks on koma ja tühik
            kassiNimed+=input() #küsime kasutajalt kassinime
            mitmes += 1 #suurendame järjekorranumbrit ühevõrra
            mituKassi -= 1 #kahandame kasside arvu mis on veel küsida ühe võrra
        
        print(kNimi, "olen kindel et "+kassiNimed+" on täitsa armsad") #kuvame kasutajale teate, kus kasutame tema nime, ja värskelt korjatud kassinimesid #et öelda kasutajale et ta kassid on armsad
    
    if(millineLoomaliik == "koer"): #kui loomaliigiks on koer
        koeraLiik = "" #muutuja mis hoiab koera liiki, hetkel tühi
        koeraNimi = "" #muutuja mis hoiab koera nime, hetkel tühi
        
        while (koeraLiik == "" or koeraNimi == ""): #tsükkel mis toimib niikaua kuni üks või teine muutja ei oma sõnet
            if koeraLiik == "": #tingimuslause mis kontrollib kas koeraliiki ei ole sisestatud
                koeraLiik = input("Palun ütle oma koera tõug") #mistõttu küsitakse kasutajalt koera liiki
            if koeraNimi == "": #tingimuslause mis kontrollib kas koera nime ei ole sisestatud
                koeraNimi = input("Palun ütle oma koera nimi") #mistõttu küsitakse kasutajalt ka koera nime, ning töödeldakse .title() abil #Esi suur Tähe Kujule
        
        print(kNimi, "teil on ilus "+koeraLiik+" koer, ",koeraNimi) #kuvame kasutajale teate, kiituslausega kus kasutame kasutaja nime, koera nime ja koera liiki

elif(kasOnLoom == "ei"): #aga kui kasutajal koduloom puudub
    kasOnKonsool = input("Kas sul on konsoole?").lower() #küsime kasutajalt kas tal on konsoole
    
    if kasOnKonsool == "ei": #kui kasutajal ei ole konsoole
        print("Head Aega") #siis kuvame lõpetusteate
    
    else: #kõigil muul juhul mis pole ei
        mituKonsooli = int(input("Mitu konsooli sul on")) #küsime kasutajalt mitu konsooli tal on
        konsooliTsükkel = mituKonsooli #teeme puhvermuutuja sellest mitu konsooli kasutajal on, kuna meil on vaja, hiljem, algset sisestust ka muutmata kujul kasutada
        konsoolid = "" #muutuja mis hoiab konsoolinimseid, samamoodi nagu kassinimseid eelnevalt, hetkel tühi
        mitmes = 1 #teksti kuvamiseks vajalik muutuja, mis kuvab küsimise järjekorranumbrit
        
        while (mituKonsooli > 0): #tsükkel mis toimib niikaua kuni kõik konsoolid on kasutaja sisestanud
            print("Sisesta oma"+str(mitmes)+". konsool") #kuvame kasutajale lause mitmendat sisestust programm ootab
            konsoolid += (input()+", ") #võtame kasutajalt sisendi, paneme ta konsoolid muutujasse, töötleme konsooli nime standardkujule ja ühtlasi paneme ka eraldaja
            mitmes += 1 #suurendame järjekorranumbrit ühe võrra
            mituKonsooli += 1 #kahandame konsoolide arvu mis on veel küsida ühe võrra
        
        if mituKonsooli > 1: #tingimuslause mis kontrollib kas kasutaja eelnevalt vastas, et tal on rohkem kui 1 konsool
            print("Go touch grass, nerd") #mille tulemusena kuvatakse kasutajale sõnum, et ta on nerd
       
       elif mituKonsooli == 1: #aga kui kasutaja eelnevalt vastas et tal on ainult 1 konsool
            print(kNimi, "loodan et oled oma"+konsoolid+"konsooliga epic gamer") #siis kuvame kasutajale teate, kasutades tema nime ja konsooli mis ta sisestas et ta on epic gamer