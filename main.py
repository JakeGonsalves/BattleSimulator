import time, sys
from entities import Swordsman, Archer, Cavalry, Spearman

class Army:
    def __init__(self):
        self.money = 5000
    def getMoney(self):
        return self.money
    def setMoney(self, money):
        self.money = money

def buyUnit():
    def swrd():
        newUnit = Swordsman()
    def arch():
        newUnit = Archer()
    def caval():
        newUnit = Cavalry()
    def spear():
        newUnit = Spearman()

    unitOpt = {0 : swrd,
               1 : arch,
               2 : caval,
               3 : spear}

    print("Select a unit to purchase\n1. Swordsman\n2. Archer\n3. Cavalry\n4. Spearman\n")
    unitChoice = input()
    newUnit = unitOpt[unitChoice]()


buyUnit()