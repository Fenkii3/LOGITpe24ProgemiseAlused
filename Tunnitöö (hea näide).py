
# NB - kõik küsimised on tsüklis, ja joonistamine toimub tkinteriga
#
# kirjuta programm mis
# küsib kasutajalt kui vana ta on
# - kui kasutaja on noorem kui 3 aastat, ütle kasutajale et on liiga noor, ning kujundit ei joonistata
# küsib kasutajalt mis on ta lemmikvärv inglise keeles
# küsib kasutajalt mis on ta lemmikkujund (tn kolmnurk, ruut, ristkülik, ring, ovaal, kaheksanurk)
# Joonista kasutaja lemmikvärvi kujund ja kirjuta kujundi keskele tema vanus

from tkinter import *

raam = Tk()
raam.title("seksikas tahvel")
tahvel = Canvas(raam, width=1000, height=1000)

vanus = ""
värv = ""
kujund = ""

while (vanus == ""):
    vanus = input("Kui vana sa oled?: ")
if int(vanus) <= 3:
    print("Sa oled liiga noor, ning kujundit ei joonistata")
if int(vanus) >= 3:
    print("Oled piisavalt vana ning joonistame sulle kujundi")

while (värv == ""):
    värv = input("Mis on su lemmikvärv, valikus punane, sinine, roheline, pruun, roosa, must, , vasta Inglise Keeles?: ")
while (kujund == ""):
    kujund = input("Mis on su lemmikkujund, kas kolmnurk, ruut, ristkülik, ring, ovaal, kaheksanurk ")

if (kujund == "kolmnurk"):
    tahvel.create_line(200,200,200,300,300,300,200,200, width=2, fill=värv)
if (kujund == "ruut"):
    tahvel.create_rectangle(10,10,110,110, outline ="black",fill =värv,width = 2)
if (kujund == "ristkülik"):
    tahvel.create_rectangle(210,10,310,210,outline ="black",fill =värv,width = 2)
if (kujund == "ring"):
    tahvel.create_oval(400,200,500,300, width = 2, outline = "black", fill = värv)
if (kujund == "ovaal"):
    tahvel.create_oval(500,200,600,500, width = 2, outline = "black", fill = värv)
if (kujund == "kaheksanurk"):
    tahvel.create_polygon(100,100,200,100,300,200,300,300,200,400,100,400,0,300,0,200, width = 2, outline = "black", fill = värv)
  
tahvel.create_text(250,250, text = vanus, fill="blue")

tahvel.pack()

raam.mainloop()