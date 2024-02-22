class Hero:

    def __init__(self, name, health, attackPower):
        self.__name = name
        self.__health = health
        self.__attackPower = attackPower
    
    # Getter
    def getName(self):
        return self.__name

    def getHealth(self):
        return self.__health

    # Setter
    def attack(self, attacking):
        self.__health -= attacking

undying = Hero("Undying", 200, 5)

print(undying.getName())
print(undying.getHealth())
undying.attack(10)
print(undying.getHealth())

