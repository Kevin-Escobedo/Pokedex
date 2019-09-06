#Class for Pokémon Types

class Type:
    def __init__(self, type1:str = None, type2:str = None):
        self.type1 = type1
        self.type2 = type2

    def __repr__(self):
        if self.type1 and self.type2:
            return "Type({}, {})".format(self.type1, self.type2)
        else:
            return "Type({})".format(self.type1)
