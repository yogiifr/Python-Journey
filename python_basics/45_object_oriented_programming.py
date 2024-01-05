class Students:

    def __init__(self, name, contact) -> None:
        self.name = name
        self.contact = contact
    
    def getdata(self):
        print("Accepting data")
        self.name = input("Enter name:")
        self.contact = input("Enter contact:")

    def putdata(self):
        print("The name is:"+self.name,"This is the contact:"+self.contact)

John = Students("blank", 0)
John.getdata()
John.putdata()