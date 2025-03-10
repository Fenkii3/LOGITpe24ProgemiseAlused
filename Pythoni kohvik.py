# Kirjuta programm mis
#
# küsib kasutajalt, palju ta panustab
# programm genereerib suvalise arvu (1-6)
# küsib kasutajalt, milline täringukülg jääb ülespoole
# võrdleb kasutaja pakkumist suvaliselt genereeritud arvuga
# kui arv on sama nagu kasutaja pakkumine,
# ütle kasutajale et: "Oled võitnud, siin on sinu <panus*5>!"
# kui arv ei ole võrdne kasutaja pakkumisega
# siis ütleme kasutajale et: "Oled kaotaja, jäid oma <panus> panusest ilma"
 
# kirjuta programm mis
#
# küsib kasutajalt kas tal on kõht tühi.
# kui kasutaja vastab ei:
#---siis programm ütleb talle vastu tagasi "ootame teid jälle kui teil isu on"
# kui kasutaja vastab ja:
#---küsib programm kas ta tahab ise võileiva kokku panna, või lasta arvutil selle genereerida
#---kui kasutaja tahab ise kokku panna, siis:
#-------küsib programm temalt kas ta tahab ühepoolset võileiba või kahepoolset võileiba:
#-------küsib programm temalt kas ta tahab võileivale võid või majoneesi
#-------küsib programm temalt kas ta tahab kurki võileivale
#-------küsib programm temalt kas ta tahab tomatit võileivale
#-------küsib programm temalt kas ta tahab peekonit võileivale
#---kui kasutaja tahab suvaliselt kokku panna, siis genereeritakse talle 5 korda erinev võileiva osa järjest
#---programm koostab kasutajale ascii pildi erinevatest kihtidest mida kasutaja lisanud on või arvuti genereerinud on
#---, ja küsib temalt raha 1.50 + 0.75 iga lisatud kihi eest
#---kui kasutaja ei maksa, siis öeldakse talle "ootame teid jälle kui teil isu on ja raha ka"
#---kui kasutaja maksab, siis tagastatakse ascii võileib teatega "aitäh tellimuse eest, tulge jälle"
# sai - [ , ,, '' ']
# või ja majoneesi jaoks ei kuvata kihti, aga ta annab hinnas lihtsalt juurde
# kurk - ▄▄▄▄ ▄▄▄
#tomat - ( | ▌|██)
#bacon - "~-,._.,-~"~-,.

from random import randint

toit = input("Tere! Kas teil on kõht tühi?")
if (toit == "Ei"):
    print("Ootame teid jälle, kui teil isu on")
else:
    if (toit == "Ja"):
        kasutajaValik = input("Kas soovite ise võileiva kokku panna, või lasete arvutil selle genereerida")
        if (kasutajaValik.lower == "ise"):
            print("Küsin sinult võileiva kohta mõned küsimused")
            sai = input("Kas sa soovid ühepoolset või kahepoolset võileiba (ühe/kahepoolne)")
            kaste = input("Kas sa soovid võileivale võid või majoneesi? (või/majo)")
            kurk = input("Kas sa soovid võileivale kurki? (jah/ei)")
            tomat = input("Kas sa soovid võileivale tomatit? (jah/ei)")
            peekon = input("Kas sa soovid võileivale peekonit? (jah/ei)")
        
        elif (kasutajaValik.lower() == "masin"):
            print("Oota kuniks võileivamasin genereerib sulle võileiva")
        
        saiRand = randint(0,1)
        kasteRand = randint(0,1)
        kurkRand = randint(0,1)
        tomatRand = randint(0,1)
        peekonRand = randint(0,1)
        
        if bool(saiRand) == True:
            sai = "kaks"
        else:
            sai = "üks"
        if bool(kasteRand) == True:
            kaste = "või"
        else:
            kaste = "majo"
        if bool(kurkRand) == True:
            kurk = "Jah"
        else:
            kurk = "Ei"
        if bool(tomatRand) == True:
            tomat = "Jah"
        else:
            tomat = "Ei"
        if bool (peekonRand) == True:
            peekon = "Jah"
        else:
            peekon = "Ei"
        if (sai == "kaks"):
            algsumma += lisand
        print("[ , ,, '' ']")
    
        
        algsumma = 1.50
        lisand = 0.75
        if(sai == "ühe"):
            algsumma = algsumma + lisand
            print("[ , ,, '' ']")
        if(kaste ==  "majo"):
            algsumma = algsumma + lisand
        if(kurk == "jah"):
            algsumma = algsumma + lisand
            print(" ▄▄▄▄ ▄▄▄")
        if(tomat == "jah"):
            algsumma = algsumma + lisand
            print("( | ▌|██)")
        if(peekon == "jah"):
            algsumma = algsumma + lisand
            print('"~-,._.,-~"~-,.')
            
        print("Siin on sinu võileib, teie lõppsummaks tuleb: " +str(algsumma)+"€")
        kasutajaValik = input ("Kas maksate?:")
        if (kasutajaValik == "Jah"):
            print("Selge, ootame teid alati tagasi.")
        else:
            if (kasutajaValik == "Ei"):
                print("Selge, järgmine kord ennem kui tellimust esitama hakkate siis kontrollige kas teil raha ka ikka on.")
            
          
        
    


    








