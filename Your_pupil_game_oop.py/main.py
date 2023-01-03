class Critter(object):
    def __init__(self, name):
        print("A critter has been born!")
        self.name = name

    def __str__(self):
        rep = "Critter object\n"
        rep += "name: " + self.name + "\n"
        return rep

    def talk(self):
        print("Hi. I'm an instance of class Critter.")

crit1 = Critter("Reksio")
crit1.talk()

crit2 = Critter("Burek")
crit2.talk()

print("Printing crit1:")
print(crit1)

print("Directly accessing crit1.name:")
print(crit1.name)

input("\n\nPress the enter key to exit.")