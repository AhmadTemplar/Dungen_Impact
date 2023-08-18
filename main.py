from random import randint
from colorama import Fore , Style

class player():
    def __init__(self,playerName):
        self.name = playerName
        self.maxHp = 500
        self.armor = 150
        self.maxEnergy = 100
        
    def attack(self):
        ...
        
print('[ ---Welcome to DUNGEN IMPACT--- ]')
ali = player('ali W')
ahmad = player('ahmad R')
