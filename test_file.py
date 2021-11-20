import random
import json

class Slovnik:
    #slovicka = dict()
    def __init__(self, slovicka=dict(), file='data.json'):
        self.slovicka = slovicka
        self.file = file

    def enter_file(self):
        enter = input('Napište název souboru: ')
        with open(enter, 'r') as a_file:
            self.slovicka = json.loads(a_file.read())
            return self.slovicka


    def add_words(self):
        while True:
            vlozit_key = input('Vložte libovolné slovíčko: ')
            if vlozit_key == '':
                break
            else:
                vlozit_value = input('Vložte jeho překlad: ')
                self.slovicka[vlozit_key] = vlozit_value

    def file_write(self):
            with open(self.file, 'w') as a_file:
                json.dump(self.slovicka, a_file)

    def file_append(self):
        slovicka_append = dict()

        while True:
            vlozit_key = input('Vložte libovolné slovíčko: ')
            if vlozit_key == '':
                break
            else:
                vlozit_value = input('Vložte jeho překlad: ')
                self.slovicka[vlozit_key] = vlozit_value
                slovicka_append[vlozit_key] = vlozit_value
        with open(self.file, "r+") as file:
            data = json.load(file)
            data.update(slovicka_append)
            file.seek(0)
            json.dump(data, file)
        exit()

    def file_open(self):
        with open(self.file, 'r') as a_file:
            self.slovicka = json.loads(a_file.read())
            return self.slovicka


    spatne_slovicka = []
    total_count = 0
    count = 0
    key_list = list(slovicka)
    random.shuffle(key_list)
    for key in key_list:
        word_input = input(f'{key} = ')
    total_count += 1
    if word_input == self.slovicka[key]:
        count += 1
        print('Správně')
    else:
        print(f"Špatně, správná odpověď je '{self.slovicka[key]}'")
        spatne_slovicka.append(word_input)


    def slovicka_mix_2(self):
        key_list = list(self.slovicka)
        random.shuffle(key_list)


u1 = Slovnik()
change_file = input('Chcete změnit slovník? y/n ')
if change_file == 'y':
    u1.enter_file()
else:
    change_in_file = input('Chcete provádět změny ve slovníku? y/n ')
    if change_in_file == 'y':
        write_or_append = input('Chcete slovník přepsat, nebo doplnit? p/d ')
        if write_or_append == 'p':
            vlozeni_slovicek()
            u1.file_write()

        elif write_or_append == 'd':
            u1.file_append()
            u1.file_open()
    else:
        u1.file_open()

u1.slovicka_mix()



