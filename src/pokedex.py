from pokemon import Pokemon
from pokemon import Type
from pokemon import Stats

def create_pokedex(file_name:open) -> dict:
    '''Creates a Pokédex from a file'''
    temp_list = []
    file = open(file_name, "r")
    for line in file:
        line = line.split("\t")
        info = []
        for item in line:
            item = item.strip()
            if item != "":
                info.append(item)
        name = info[0]
        types = info[1].split("/")
        stats = info[2].split("/")

        if len(types) == 2:
            temp_list.append(Pokemon(name, Type(types[0], types[1]), Stats(int(stats[0]), int(stats[1]),
                int(stats[2]), int(stats[3]), int(stats[4]), int(stats[5]))))

        else:
            temp_list.append(Pokemon(name, Type(types[0]), Stats(int(stats[0]), int(stats[1]),
                int(stats[2]), int(stats[3]), int(stats[4]), int(stats[5]))))

    file.close()

    pokedex = dict()

    for i, pokemon in enumerate(temp_list):
        pokedex[i+1] = pokemon

    return pokedex

if __name__ == "__main__":
    pokedex = create_pokedex("pokedex.txt")
