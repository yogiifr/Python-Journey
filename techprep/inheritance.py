# Pewarisan / Hal yang diturunkan kelas ke kelas
# Class 1 - Super Class
# Class 2 - Sub Class

# Super Class
class Hero:

    def __init__(self, name, health):
        self.name = name
        self.health = health

# Sub Class
class Hero_Int(Hero):
    pass

class Hero_Str(Hero):
    pass

lina = Hero("Lina", 100)
techies = Hero_Int("Techies", 75)
axe = Hero_Str("Axe", 200)

print(lina.name)
print(techies.name)
print(axe.name)