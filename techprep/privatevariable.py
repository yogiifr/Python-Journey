class Hero:

    # Class Variable
    jumlah = 0

    __privateJumlah = 0

    def __init__(self, name, health):
        self.name = name
        self.health = health

        # Variable Instance Private
        self.__private = "private"
        self._protected = "protected"


lina = Hero("Lina", 100)

print(lina.__dict__)
print(Hero.__dict__)