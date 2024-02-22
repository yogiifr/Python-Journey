class Hero:

    # Private Class Variable
    __jumlah = 0

    def __init__(self, name, health, power, armor):
        self.__name = name
        self.__healthStandar = health
        self.__attPowerStandar = power
        self.__armorStandar = armor
        self.__level = 1
        self.__exp = 0

        self.__healthMax = self.__healthStandar * self.__level
        self.__attPower = self.__attPowerStandar * self.__level
        self.__armor = self.__armorStandar * self.__level

        self.__health = self.__healthMax

        Hero.__jumlah += 1
    
    @property
    def info(self):
        return f"{self.__name} .Lvl-{self.__level} .exp-{self.__exp}: \n\tHealth = {self.__health}/{self.__healthMax} \n\tAttack = {self.__attPower} \n\tArmor = {self.__armor}"
    
    @property
    def gainExp(self):
        pass

    @gainExp.setter
    def gainExp(self, addExp):
        self.__exp += addExp
        if (self.__exp >= 100):
            print(self.__name, "Level Up!!")
            self.__level += 1
            self.__exp -= 100

            self.__healthMax = self.__healthStandar * self.__level
            self.__health = self.__healthMax
            self.__attPower = self.__attPowerStandar * self.__level
            self.__armor = self.__armorStandar * self.__level

    def attack(self, enemy):
        self.gainExp = 50

slardar = Hero('Slardar', 100, 5, 10)
axe = Hero('Axe', 100, 5, 10)
print(slardar.info)

slardar.attack(axe)
slardar.attack(axe)
slardar.attack(axe)
slardar.attack(axe)
slardar.attack(axe)
slardar.attack(axe)

print(slardar.info)