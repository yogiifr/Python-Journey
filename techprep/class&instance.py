# Template
class Hero:

    # Class Variable / Static Variable
    jumlah = 0

    def __init__(self, name, health, power, armor):
        # Instance Variable / Attribute
        self.name = name
        self.health = health
        self.power = power
        self.armor = armor

        Hero.jumlah += 1

        print("Membuat Hero dengan nama " + name)

hero1 = Hero("Sniper", 100, 10, 4)
hero2 = Hero("Mirana", 100, 10, 5)

print(hero1.__dict__)
print(hero2.__dict__)
print(Hero.__dict__)
