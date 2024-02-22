class Hero: #Template
    pass


hero1 = Hero() # Object / Instancesiate
hero2 = Hero()

hero1.name = "Sniper"
hero1.health = 100

hero2.name = "Drow"
hero2.health = 300

print(hero1.__dict__)