import random
import json

slovicka = dict()


def enter_file():
    enter = input('Napište název souboru: ')
    try:
        with open(enter, 'r') as a_file:
            slovicka = json.loads(a_file.read())
        return slovicka
    except:
        with open(enter, 'w+') as b_file:
            slovicka_1 = dict()
            slovicka = dict(json.dump(slovicka_1, b_file))
            return slovicka


def vlozeni_slovicek():
    while True:
        vlozit_key = input('Vložte libovolné slovíčko: ')
        if vlozit_key == '':
            break
        else:
            vlozit_value = input('Vložte jeho překlad: ')
            slovicka[vlozit_key] = vlozit_value


def file_write():
    try:
        a_file = open('data.json', 'w')
        json.dump(slovicka, a_file)
        a_file.close()
    except:
        print('Chyba, nemáte povolení měnit text v souboru.')
        exit()


def file_append():
    slovicka_append = dict()

    while True:
        vlozit_key = input('Vložte libovolné slovíčko: ')
        if vlozit_key == '':
            break
        else:
            vlozit_value = input('Vložte jeho překlad: ')
            slovicka[vlozit_key] = vlozit_value
            slovicka_append[vlozit_key] = vlozit_value
    with open("data.json", "r+") as file:
        data = json.load(file)
        data.update(slovicka_append)
        file.seek(0)
        json.dump(data, file)
    exit()


def file_open(soubor):
    with open(soubor, 'r') as a_file:
        slovicka = dict(json.loads(a_file.read()))
        return slovicka


vstup_3 = input('Chcete změnit slovník? y/n ')
if vstup_3 == 'y':
    enter_file()
else:
    vstup = input('Chcete provádět změny ve slovníku? y/n ')
    if vstup == 'y':
        vstup_2 = input('Chcete slovník přepsat, nebo doplnit? p/d ')
        if vstup_2 == 'p':
            vlozeni_slovicek()
            file_write()

        elif vstup_2 == 'd':
            file_append()
            file_open()
    else:
        slovicka = file_open('data.json')


key_list = list(slovicka)

random.shuffle(key_list)

spatne_slovicka = []
total_count = 0
count = 0
for key in key_list:
    int = input(f'{key} = ')
    total_count += 1
    if int == slovicka[key]:
        count += 1
        print('Správně')
    else:
        print(f"Špatně, správná odpověď je '{slovicka[key]}'")
        spatne_slovicka.append(int)

print(f'Vaše špatné odpovědi: {spatne_slovicka}')
print(f'Počet bodů je {count}/{total_count}')

if total_count == 0:
    print('...')
else:
    vysledek = ((count / total_count) * 100)
    print(f'{vysledek}%')

    a = 90.5
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
        print('Tvoje znamka je 5!')
