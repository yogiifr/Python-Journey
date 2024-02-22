class Hero:

    def __init__(self, name, health):
        self.name = name
        self.health = health

    def showInfo(self):
        print(f"{self.name} with Health: {self.health}")

class Hero_Int(Hero):
    
    def __init__(self, name):
        # self.name = name
        # self.health = 100
        super().__init__(name, 100)
        super().showInfo()

class Hero_Str(Hero):
    
    def __init__(self, name):
        # self.name = name
        # self.health = 200
        super().__init__(name, 200)
        super().showInfo()

lina = Hero_Int("Lina")
axe = Hero_Str("Axe")

print(f"{lina.name} {lina.health}")
print(f"{axe.name} {axe.health}")