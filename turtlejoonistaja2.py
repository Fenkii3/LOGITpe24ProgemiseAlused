from turtle import *

fail = open("turtlejuhis.txt")

andmedfailist = []

for rida in fail:
    andmedfailist.append(rida.split())
fail.close()
    
print(andmedfailist)

if andmedfailist[0] != "edasi" or andmedfailist[0] != "paremale" or andmedfailist[0] != "vasakule" or andmedfailist[0] != "tagasi":
    color(andmedfailist[0])
  
suund = ""
arv = 0
i = 1
begin_fill()
while i < len(andmedfailist):
    osad = andmedfailist[i]
    print(osad)

    if osad[0] == "edasi":
            suund = "forward"
    elif osad[0] == "tagasi":
            suund = "back"
    elif osad[0] == "paremale":
            suund = "right"
    elif osad[0] == "vasakule":
            suund = "left"
    if (type(osad[1]) == type("string")):
        arv = int(osad[1])
    
    if suund == "forward":
        forward(arv)
        print(arv)
    elif suund == "back":
        back(arv)
        print(arv)
    elif suund == "right":
        right(arv)
        print(arv)
    elif suund == "left":
        left(arv)
        print(arv)
    i+=1
end_fill()