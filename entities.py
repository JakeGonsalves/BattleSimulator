# Units
class Unit:
    def __init__(self, health, attack, cost):
        self.health = 0
        self.attack = 0
        self.cost = 0

    # Getters
    def getHealth(self):
        return self.health

    def getAttack(self):
        return self.attack

    def getCost(self):
        return self.cost

    # Setters
    def setHealth(self, health):
        self.health = health

    def setAttack(self, attack):
        self.attack = attack

    def setCost(self, cost):
        self.cost = cost


class Swordsman(Unit):
    def __init__(self):
        super().__init__(250, 30, 50)


class Archer(Unit):
    def __init__(self):
        super().__init__(100, 80, 100)


class Cavalry(Unit):
    def __init__(self):
        super().__init__(400, 50, 200)


class Spearman(Unit):
    def __init__(self):
        super().__init__(200, 20, 80)