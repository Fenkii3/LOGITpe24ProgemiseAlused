# kirjuta programm mis
# küsib kasutajalt tema nime | küsimine toimub tsüklis
# küsib kasutajalt suvalist arvu vahemikus 1-20
# programm genereerib kasutajale kujundi, vastavalt sellele mis kasutaja on sisestanud
# kui kasutaja on sisestanud sama arvu nagu programm ette on genereerinud, siis joonistatakse kujundile roosa taust
# võimalikud kujundid on ristkülik, romb, rööpkülik ja täisnurkne kolmnurk
# võimalikud värvid on punane, kollane, roheline, sinine, oranz
# iga arvu kohta on oma kujundi-värvi kombinatsioon
# vastavalt arvule joonistatakse kasutajale seda värvi kujund | joonistamine on tsüklis ✅
# peale kujundi joonistamist kirjutatakse kujundile kasutaja nimi
 
#teksti kirjutamise jaoks on write("tekstsiia")

from random import randint
from turtle import *

nimi = ""
suvalineArv = 0

while(nimi == ""):
    nimi = input("Sisestage oma nimi: ")


    kasutajaarv = 0
    while(kasutajaarv < 1 or kasutajaarv > 20):
        kasutajaarv = int(input("Sisesta arv vahemikus 1-20"))
        randomarv = randint(1,20)
        
        if(kasutajaarv == randomarv):
            bgcolor("pink")
            # taust
        
        if(kasutajaarv == 1 or kasutajaarv == 6 or kasutajaarv == 11 or kasutajaarv == 16):
            color("red")
        elif(kasutajaarv == 2 or kasutajaarv == 7 or kasutajaarv == 12 or kasutajaarv == 17):
            color("orange")
        elif(kasutajaarv == 3 or kasutajaarv == 8 or kasutajaarv == 13 or kasutajaarv == 18):
            color("yellow")
        elif(kasutajaarv == 4 or kasutajaarv == 9 or kasutajaarv == 14 or kasutajaarv == 19):
            color("green")
        elif(kasutajaarv == 5 or kasutajaarv == 10 or kasutajaarv == 15 or kasutajaarv == 20):
            color("blue")
            
            
            
        begin_fill()
        if(kasutajaarv > 0 and kasutajaarv < 6):
            #ristkülik
            küljed = 4
            while(küljed > 0):
                if(küljed % 2 == 0):
                    forward(200)
                else:
                    forward(100)
                right(90)
                küljed -= 1
                
        elif(kasutajaarv > 5 and kasutajaarv < 11):
            # romb
            lt(45)
            küljed = 4
            while(küljed > 0):
                forward(100)
                right(90)
                küljed -= 1
        elif(kasutajaarv > 10 and kasutajaarv < 16):
            # rööpkülik
            küljed = 4
            while(küljed > 0):
                if(küljed % 2 == 0):
                    forward(200)
                else:
                    right(20)
                    forward(75)
                    left(20)
                right(90)
                küljed -= 1
        elif(kasutajaarv > 15 and kasutajaarv < 21):
            # tn kolmnurk
            print("")
            küljed = 2
            while(küljed > 0):
                left(90)
                forward(100)
                küljed -= 1
        end_fill()
    exitonclick()

    
        