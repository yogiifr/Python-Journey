# Template
class Hero:

    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

hero1 = Hero("Sniper", 100, 10)
hero2 = Hero("Mirana", 100, 10)

print(hero1.__dict__)
print(hero2.__dict__)

