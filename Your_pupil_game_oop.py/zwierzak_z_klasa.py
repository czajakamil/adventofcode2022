class Critter(object):
    total = 0

    @staticmethod
    def status():   
        print("The total number of critters is", Critter.total)

    def __init__(self, name):
        print("A critter has been born!")
        self.name = name
        Critter.total += 1

print("Accessing the class Critter attribute Critter.total:", end=" ")
print(Critter.total)

print("Creating critters.")
crit1 = Critter("Reksio")
crit2 = Critter("Burek")
crit3 = Critter("Filemon")

Critter.status()

print("Accessing the class Critter attribute through an object:", end=" ")
print(crit1.total)
input("\n\nPress the enter key to exit.")
