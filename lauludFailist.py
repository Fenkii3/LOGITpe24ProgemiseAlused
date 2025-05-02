# kirjuta programm mis
# loeb failist laulusõnu (ise valid laulu)
# kuvab välja kõik sõnad
# arvutab kokku mitu täishäälikut on (aeiouõäöüy)
# kuvab välja kõik sõnad mis on pikemad kui 7 tähte
# laseb kasutajal kirjutada ise ühe värsi (4 rida) juurde

fail = open("laulud.txt", encoding = "UTF-8")
sõnad = []
täiskokku = 0

for rida in fail:
    sõnad.append(rida)
    print(rida)

for rida in sõnad:
    täiskokku += rida.count('a')
    täiskokku += rida.count('e')
    täiskokku += rida.count('i')
    täiskokku += rida.count('o')
    täiskokku += rida.count('u')
    täiskokku += rida.count('õ')
    täiskokku += rida.count('ä')
    täiskokku += rida.count('ö')
    täiskokku += rida.count('ü')
print("Täishääikuid on kokku: " +str(täiskokku))

for rida in sõnad:
    for sõna in rida.split():
        if len(sõna) > 7:
            print(sõna)
    
for x in range(4):
    sõnad.append(input("Sisesta ise uus värss: "))
for rida in fail:
    sõnad.append(rida)
    print(rida)