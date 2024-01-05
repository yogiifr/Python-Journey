class MyClass:
    __hiddenvariable = 0

    def add(self, increment):
        self.__hiddenvariable += increment
        print(self.__hiddenvariable)

object1 = MyClass()
object1.add(5)

print(object1.__hiddenvariable)
