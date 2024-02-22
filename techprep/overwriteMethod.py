class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health
    
    def showInfo(self):
        print(f"{self.name} \nHealth:{self.health}")

class Hero_Int(Hero):
    def __init__(self, name):
        super().__init__(name, 100)
        # Override
        print(f"{self.name} \nHealth:{self.health} \nType: Intelegence")

class Hero_Str(Hero):
    def __init__(self, name):
        super().__init__(name, 200)


lina = Hero_Int("Lina")
axe = Hero_Str("Axe")

lina.showInfo()
axe.showInfo()