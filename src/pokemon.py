#Class for Pokemon
import type_class
import stats_class

class Pokemon:
    def __init__(self, name:str = "", types:type_class.Type = type_class.Type(), stats:stats_class.Stats = stats_class.Stats()):
        self.name = name
        self.type = types
        self.stats = stats
