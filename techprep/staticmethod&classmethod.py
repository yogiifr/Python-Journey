class Hero:

    # Private Class Variable
    __jumlah = 0

    def __init__(self, name):
        self.__name = name
        Hero.__jumlah += 1

    # Berlaku untuk object
    def getJumlah(self):
        return Hero.__jumlah
    
    # Berlaku untuk class
    def getJumlah():
        return Hero.__jumlah

    # Method Static (Decorator)
    @staticmethod
    def getJumlah2():
        return Hero.__jumlah

    @classmethod
    def getJumlah3(cls):
        return cls.__jumlah


sniper = Hero("Sniper")
drow = Hero("Drow")

print(Hero.getJumlah())

print(sniper.getJumlah2())
print(Hero.getJumlah2())

print(sniper.getJumlah3())
print(Hero.getJumlah3())