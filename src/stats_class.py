#Class for Pokémon Base Stats

class Stats:
    def __init__(self, HP:int = 0, ATK:int = 0, DEF:int = 0, SPATK:int = 0, SPDEF:int = 0, SPE:int = 0):
        self.HP = HP
        self.ATK = ATK
        self.DEF = DEF
        self.SPATK = SPATK
        self.SPDEF = SPDEF
        self.SPE = SPE

    def __repr__(self):
        return "Stats({}, {}, {}, {}, {}, {})".format(self.HP,
                                                      self.ATK,
                                                      self.DEF,
                                                      self.SPATK,
                                                      self.SPDEF,
                                                      self.SPE)
