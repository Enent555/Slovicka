import random
import json

slovicka = dict()

def vlozeni_slovicek():
    while True:
        vlozit_key = input('Vložte libovolné slovíčko: ')
        if vlozit_key == '':
            #print(slovicka)
            break
        else:
            vlozit_value = input('Vložte jeho překlad: ')
            slovicka[vlozit_key] = vlozit_value
        #for key, value in slovicka.items():
            #print('Slovo: {}, Preklad: {}'.format(key, value))
        #print(slovicka)
vlozeni_slovicek()

def file_write():
    a_file = open('data.json','w')
    json.dump(slovicka,a_file)
    a_file.close()
file_write()

a_file = open('data.json','r')
output = a_file.read()
# print(output)



"""
slovicka = {'dobrodružný':'abenteuerlich', 'jiný, ostatní':'ander', 'horský průvodce':'der Bergfuhrer',
            'jedinečný':"einzigartig", "zkušený":"erfahren", "vrchol":"der Gipfel",
            "milovník, milenec":"der Liebhaber", "spisovatel": "der Schriftseller",
            "cesta, stezka":"die Strecke", "různé druhy sportu":"verschiedene Sportarten",
            "náročný":"anspruchsvoll", "vyznat se":"sich aus/kennen", "oba":"beide",
            "horolezec":"der Bergsteiger", "někteří, nějací":"einige", "soupeř, "
            "protivník":"der Gegner", "túra":"der Tour","poskytnout první pomoc":"Erste Hilfe leisten",
            "málo zkušeností":"wenige Erfahrungen", "mnozí sportovci":"manche Sportler"}
"""
key_list = list(slovicka)

random.shuffle(key_list)

spatne_slovicka = []
total_count = 0
count = 0
for key in key_list:
    int = input(f'{key} = ')
    total_count = total_count + 1
    if int == slovicka[key]:
        count = count + 1
        print('Správně')
    else:
        print(f"Špatně, správná odpověď je '{slovicka[key]}'")
        spatne_slovicka.append(int)
        # int_2 = input('Opiš to slovíčko: ')
        # if int_2 != v:
        # print('Ty jsi ale debil!')

print(f'Vaše špatné odpovědi: {spatne_slovicka}')
print(f'Počet bodů je {count}/{total_count}')
vysledek = ((count/total_count)*100)
print(f'{vysledek}%')
a = 90
b = 80
c = 70
d = 60
if vysledek >= a:
    print('Tvoje známka je 1!')
elif vysledek < a and vysledek >= b:
    print('Tvoje znamka je 2!')
elif vysledek < b and vysledek >= c:
    print('Tvoje znamka je 3!')
elif vysledek < c and vysledek >= d:
    print('Tvoje znamka je 4!')
elif vysledek < d:
    print('Máš bůra!')
