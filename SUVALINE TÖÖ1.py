# kirjuta programm mis
#
# küsib kasutajalt tema nime | tegevus on tsüklis | nimi mida kontrollima peab on Siim
# küsib kasutajalt tema perekonnanime | tegevus on tsüklis | nimi mida kontrollima peab on Kallas
# nii kasutaja ees, kui ka perekonnanimi peab olema õige. Selle jaoks saab kasutada loogilist tehet,
# ning kasutajasisestus tuleb töödelda läbi funktsiooniga .capitalize()
# küsib kasutajalt esimest pin koodi | tegevus on tsüklis (ei tohi olla 0000 ega 1234)
# küsib kasutajalt ühte kolmest tegevusest mida ta teha soovib: | tegevus on tsüklis
# tegevused on: konto jäägi vaatamine, seifis oleva kulla koguse vaatamine, ja tehingu tegemin
# kui kasutaja valib konto jäägi vaatamise, siis tagastatakse kasutajale sõnum, tema konto jäägiga
# kui kasutaja valib eifis oleva kulla koguse vaatamise, siis küsitakse kasutajalt teist pin koodi
# - kui pin kood on õige, näidatakse kasutajale tema kulla kogust, programm väljastab tsüklis
# - ascii artina igale reale kullakangi niipalju kui neid on. | tegevus on tsüklis, väljastatakse vajalik kogus ridu
# kui kasutaja valib konto jäägi vaatamitehingu tegemise, siis küsitakse kasutajalt mõlemat pin koodi kahe küsimusega | tegevus on tsüklis
# ning kui mõlemad on õiged, alles siis lastakse kasutaja tehingumenüü juurde | tegevus on tsüklis
# - tehingumenüüs on 2 valikut:
# - välju (mis lõpetab programmi sõnumiga "headaega <eesnimi><perekonnanimi>, järgmise korrani, teie kuld on ohutult hoiul meie juures"
# - ülekanne
# - kui kasutaja valib ülekanne siis:
# - - küsitakse temalt saaja ees ja perekonnanime, teist pin koodi, kui palju raha ja kui palju kulda ta üle kanda soovib: | tegevus on tsüklis



Nimi1 = "Siim"
Nimi2 = ""
perekonnanimi = "Kallas"
perekonnanimi1 = ""
kontijääkKroonides = 10000000
kullajääkKGKangides = 420

while (Nimi2 != Nimi1):
    Nimi2 = input("Tere tulemast kullaautomaati, palun sisesta oma nimi: ").capitalize()
    
while (perekonnanimi1 != perekonnanimi):
        perekonnanimi1 = input("Palun sisesta oma perekonnanimi ka: ").capitalize()

if (Nimi2 == Nimi1 and perekonnanimi1 == perekonnanimi):
    correctPin1 = 4545
    correctPin2 = 6767
    kasutajaPin1 = int(input("Palun sisesta pinkood #1"))
    if (kasutajaPin1 == 0000 or kasutajaPin1 == 1234):
        print("Neid pin-koode pole lubatud masinasse sisestada")
    elif (kasutajaPin1 == correctPin1):
        kasutajaTegevus = ""
        while (kasutajaTegevus == ""):
            kasutajaTegevus = input("Palun valige tegevus: \n== Vaata konto jääki == 'konto'\n== Vaata seifi kulda == 'kuld'\n== Tee tehing            == 'tehing'")
            if(kasutajaTegevus.lower() != "konto" or kasutajaTegevus.lower() == "kuld" or kasutajaTegevus.lower() == "tehing"):
                if(kasutajaTegevus.lower() == "konto"):
                    print("Palun "+Nimi2+" "+perekonnanimi1+", teie konto jääk on: "+str(kontojääkKroonides)+" krooni.")
                elif(kasutajaTegevus.lower() == "kuld"):
                    kasutajaPin2 = int(input("Palun sisesta pin-kood #2 edasiminemiseks."))
                    if (kasutajaPin1 == 0000 or kasutajaPin2 == 1234):
                        print("Masin ei võta vastu lihtsaid pin koode, nagu 0000 või 1234")
                    elif (kasutajaPin2 == correctPin2):
                        increment = 0
                        while (increment != kullajääkKGKangides):
                            print("/_\\__24k_1kg____\\")
                            increment += 1
                        print("Palun "+Nimi2+" "+perekonnanimi1+", seifis on teil kulda: "+str(kullajääkKGKangides)+" kilo.")
                    elif (kasutajaTegevus.lower() == "tehing"):
                        kastuajaPin1 = 0
                        kasutajaPin2 = 0
                        while(KasutajaPin1 == 0 or kasutajaPin2 == 0):
                            if (kasutajaPin1 == 0):
                                kasutajaPin1 = int(input("Palun sisesta pin-kood #1 uuesti"))
                            if (kasutajaPin2 == 0):
                                kasutajaPin2 = int(input("Palun sisesta pin-kood #2 uuesti"))
# kui kasutaja valib tehingu tegemise, siis küsitakse kasutajalt mõlemalt pin koodi kahe küsimusega, tegevus on tsüklis

# ning kui mõlemad on õiged, alles siis lastakse kasutaja tehingumenüü juurde, tegevus on tüsklis
                    if (kasutajaPin1 == correctPin1 and kasutajaPin2 == correctPin2):
                        menüüValik = ""
                        while (menüüValik == ""):
                            print("Tehingumenüü: Vali tegevus\n== Ülekanne == 'ük'\n== Välju      == 'xt'")
                        menüüValik == input()
                        if (menüüvalik == "ük"):
                            #küsitakse temalt saaja ees ja perekonnanime,
                            # teist pin koodi, kui palju raha ja kui palju kulda
                            # ta üle kanda soovib:, tegevus on tsüklis
                            
                        
                        else:
                            print("Head aega "+Nimi2+" "+perekonnanimi1+", järgmise korrandi, teie kuld on ohutult hoiul meie juures")
                        
           else:
                print("Palun sisesta õigesti kirjutatud valik")
                kasutajaTegevus = ""


    else:
        print("Pin-kood on vale!")
