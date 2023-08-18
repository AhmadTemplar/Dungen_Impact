from random import randint
from colorama import Fore , Style

class player():
    def __init__(self,playerName):
        self.name = playerName
        self.maxHp = 500
        self.armor = 150
        self.maxEnergy = 100
        self.maxDamage = 110
        self.minDamage = 50
    def attack(self):
        dmg = randit(self.minDamage, self.maxDamage)
        return dmg
        
print('[ ---Welcome to DUNGEN IMPACT--- ]')
ali = player('ali W')
ahmad = player('ahmad R')

dmg = ali.attack()
