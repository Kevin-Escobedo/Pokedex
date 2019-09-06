#Class for Pokemon
from type_class import Type
from stats_class import Stats

class Pokemon:
    def __init__(self, name:str = "", types:Type = Type(), stats:Stats = Stats()):
        self.name = name
        self.type = types
        self.stats = stats

    def __repr__(self):
        return "Pokemon({}, {}, {})".format(self.name, self.type, self.stats)


if __name__ == "__main__": #Cleanup later
    file = open("pokedex.txt", "r")
    a_pokedex = []
    for line in file:
        line = line.split("\t")
        info = []
        for item in line:
            if item.strip() != "":
                info.append(item.strip())
        name = info[0]
        types = info[1].split("/")
        stats = info[2].split("/")

        if len(types) == 2:
            a_pokedex.append(Pokemon(name, Type(types[0], types[1]), Stats(int(stats[0]), int(stats[1]),
                                                                         int(stats[2]), int(stats[3]),
                                                                         int(stats[4]), int(stats[5]))))
        else:
            a_pokedex.append(Pokemon(name, Type(types[0]), Stats(int(stats[0]), int(stats[1]),
                                                               int(stats[2]), int(stats[3]),
                                                               int(stats[4]), int(stats[5]))))
    file.close()

    pokedex = dict()

    for i, pokemon in enumerate(a_pokedex):
        pokedex[i+1] = pokemon

    
