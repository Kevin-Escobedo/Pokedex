#Author: Kevin C. Escobedo
#Email: escobedo001@gmail.com
import sqlite3

class Pokedex:
    def __init__(self, database:str = "pokedex.db"):
        '''Constructor for Pokédex'''
        self.db = sqlite3.connect("{}".format(database))
        self.cursor = self.db.cursor()

    def create_table(self, table_name:str) -> None:
        '''Creates a new table in the database'''
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS {}(dex_num INTEGER PRIMARY KEY, name TEXT, type1 TEXT, type2 TEXT, HP INTEGER, Attack INTEGER, Defense INTEGER, SpecialAttack INTEGER, SpecialDefense INTEGER, Speed INTEGER, total INTEGER)""".format(table_name))

        self.db.commit()

    def insert_pokemon(self, table_name:str, num:int, name:str, types:tuple, stats:list) -> None:
        '''Inserts a Pokémon into a table'''
        try:
            self.cursor.execute("""INSERT INTO {}(dex_num, name, type1, type2, HP, Attack, Defense, SpecialAttack, SpecialDefense, Speed, total) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""".format(table_name), (num, name, types[0], types[1], stats[1], stats[2], stats[3], stats[4], stats[5], stats[6], stats[0]))
        except sqlite3.IntegrityError:
            pass

    def close(self) -> None:
        '''Closes the database'''
        self.db.commit()
        self.db.close()


def get_names():
    file = open("pokedex.txt", "r")
    info = file.readlines()
    file.close()
    outfile = open("pokemon_names.txt", "w")
    for data in info:
        data = data.split("\t")
        name = data[0].split(".")[1].strip()
        outfile.write("{}\n".format(name))
    outfile.close()
    
def add_entry(p:Pokedex) -> None:
    '''Adds entries to the Pokédex'''
    file = open("pokedex.txt", "r")
    p.create_table("national_dex")
    p.create_table("gen_1")
    gen_1_count = 1
    p.create_table("gen_2")
    gen_2_count = 1
    p.create_table("gen_3")
    gen_3_count = 1
    p.create_table("gen_4")
    gen_4_count = 1
    p.create_table("gen_5")
    gen_5_count = 0
    p.create_table("gen_6")
    gen_6_count = 1
    p.create_table("gen_7")
    gen_7_count = 1
    info = file.readlines()
    file.close()
    for i, data in enumerate(info):
        data = data.split("\t")
        name = data[0].split(".")[1].strip()
        type1 = data[1].split("/")[0]
        try:
            type2 = data[1].split("/")[1]
        except IndexError:
            type2 = ""
        types = (type1, type2)
        hp = int(data[2].split("/")[0])
        atk = int(data[2].split("/")[1])
        defe = int(data[2].split("/")[2])
        spatk = int(data[2].split("/")[3])
        spdef = int(data[2].split("/")[4])
        speed = int(data[2].split("/")[5])

        total = int(data[3].split(": ")[1])

        stats = [total, hp, atk, defe, spatk, spdef, speed]

        dex_num = i+1

        if dex_num <= 151:
            p.insert_pokemon("gen_1", gen_1_count, name, types, stats)
            gen_1_count += 1
        elif dex_num > 151 and dex_num <= 251:
            p.insert_pokemon("gen_2", gen_2_count, name, types, stats)
            gen_2_count += 1
        elif dex_num > 251 and dex_num <= 386:
            p.insert_pokemon("gen_3", gen_3_count, name, types, stats)
            gen_3_count += 1
        elif dex_num > 386 and dex_num <= 493:
            p.insert_pokemon("gen_4", gen_4_count, name, types, stats)
            gen_4_count += 1
        elif dex_num > 493 and dex_num <= 649:
            p.insert_pokemon("gen_5", gen_5_count, name, types, stats)
            gen_5_count += 1
        elif dex_num > 649 and dex_num <= 721:
            p.insert_pokemon("gen_6", gen_6_count, name, types, stats)
            gen_6_count += 1
        elif dex_num > 721 and dex_num <= 809:
            p.insert_pokemon("gen_7", gen_7_count, name, types, stats)
            gen_7_count += 1

        p.insert_pokemon("national_dex", dex_num, name, types, stats)

        


if __name__ == "__main__":
    p = Pokedex()
    #get_names()
    p.close()


