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
        res = randit(self.minDamage, self.maxDamage)
        return res
            
    def heal(self):
    res = self.maxHp*40/100
    self.maxHp += res
    return res
    
print('[ ---Welcome to DUNGEN IMPACT--- ]')
ali = player('ali W')
ahmad = player('ahmad R')

dmg = ali.attack()
ahmad.maxHp -= dmg

# majbor shodam beram dash , bye
# no problme , Bye
