class Hero:
    
    def __init__(self, name, health, attackPower, armorNumber):
        self.name = name
        self.health = health
        self.attackPower = attackPower
        self.armorNumber = armorNumber
    
    def attack(self, hero):
        print(f"{self.name} Attacking {hero.name}")
        print(f"{hero.name} Attacked by {self.name}")

        damage = self.attackPower / hero.armorNumber
        print(f"Damage output {damage}")

        hero.health -= damage
        print(f"Curent health of {hero.name} is {hero.health}")


sniper = Hero("Sniper", 50, 15, 5)
drow = Hero("Drow", 75, 12, 7)

sniper.attack(drow)
print("\n")
drow.attack(sniper)