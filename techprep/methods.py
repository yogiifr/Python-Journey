# Template
class Hero:

    # Class Variable / Static Variable
    jumlah = 0

    def __init__(self, name, health, power, armor):
        # Instance Variable / Attribute
        self.Name = name
        self.Health = health
        self.Power = power
        self.Armor = armor

        Hero.jumlah += 1
    
    # Void function, method tanpa return
    def siapa(self):
        print("Namaku adalah " + self.Name)

    # Method dengan argumen
    def healthUp(self, up):
        self.Health += up
    
    # Method dengan return
    def getHealth(self):
        return self.Health

hero1 = Hero("Sniper", 100, 10, 4)
hero2 = Hero("Mirana", 100, 10, 5)

print(hero1.__dict__)
print(hero2.__dict__)

hero1.siapa()
hero1.healthUp(10)
print(hero1.getHealth())