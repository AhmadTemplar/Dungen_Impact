from random import randint
from colorama import Fore , Style

class player():
    def __init__(self,playerName):
        self.name = playerName
        self.maxHp = 500
        self.armor = 150
        self.maxEnergy = 100

input(f'= = = [ ---Welcome to DUNGEN IMPACT--- ] = = =\nhehe')
ahmad = player('Master Moonlight')
print(ahmad.name,ahmad.maxHp,ahmad.armor,ahmad.maxEnergy)
