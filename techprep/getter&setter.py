class Hero:

    def __init__(self, name, health, armor):
        self.name = name
        self.__health = health
        self.__armor = armor
    
    @property
    def info(self):
        return f"Name {self.name} : \n\t Health: {self.__health}"

    @property
    def armor(self):
        pass

    @armor.getter
    def armor(self):
        return self.__armor
    
    @armor.setter
    def armor(self, input):
        self.__armor = input
    
    @armor.deleter
    def armor(self):
        print('Armor di delete')
        self.__armor = None
    
sniper = Hero("Sniper", 10, 5)

print(sniper.info)

sniper.name = "Asep"
print(sniper.info)

print("Getter dan setter untuk __armor: ")
print(sniper.armor)

sniper.armor = 50
print(sniper.armor)

print("Deleting armor")
del sniper.armor

print(sniper.__dict__)