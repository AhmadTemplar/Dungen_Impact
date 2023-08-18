from random import randint
from colorama import Fore , Style
from json import loads,dumps

class player():
    def __init__(self,playerName):
        self.name = playerName
        self.maxHp = 500
        self.armor = 150
        self.maxEn = 100
        self.maxDmg = 110
        self.minDmg = 50
        
    def attack(self):
        '''Generats Random int and Return it
        * min/max Chose from init func'''

        res = randit(self.minDmg, self.maxDmg)
        return res

    def criticalAttack(self):
        '''Its like attack func But int Boosted 23%'''

        res = self.attack()*123/100
        return res
        
    def heal(self):
        '''Increase selfHp 40% and Decrease selfEn 25 Point'''

        res = self.maxHp*40/100
        self.maxHp += res
        self.maxEn -= 15
        return res
    
print('<[ ---Welcome to DUNGEN IMPACT--- ]>')
ali = player('ali W')
ahmad = player('ahmad R')