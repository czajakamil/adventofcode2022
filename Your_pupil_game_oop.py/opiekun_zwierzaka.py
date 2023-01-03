class Critter(object):
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
    
    def __str__(self):
        return  f"\nImię zwierzaka: {self.name}\n" \
                f"Poziom głodu: {self.hunger}\n" \
                f"Poziom nudy: {self.boredom}\n"
    
    # _ metoda prywatna - nie można jej wywołać z zewnątrz
    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    """ @property pozwala nam na wywołanie metody bez nawiasów
    np. print(crit1.mood) zamiast print(crit1.mood()) 
    Zwykle używamy @property wtedy, gdy chcemy zwrócić wartość atrybutu, 
    a nie wykonać jakieś działanie.
    """
    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "szczęśliwy"
        elif 5 <= unhappiness <= 10:
            m = "zadowolony"
        elif 11 <= unhappiness <= 15:
            m = "zły"
        else:
            m = "wściekły"
        return m

    def talk(self):
        print("Nazywam się", self.name, "i jestem teraz", self.mood, "\n")
        self.__pass_time()
    
    def eat(self, food_input = 4):
        print(f"Aktualny poziom głodu: {self.hunger}")
        while True:
            try:
                food_input = int(input("Ile jedzenia chcesz podać? (1-10) "))
                if food_input < 1 or food_input > 10:
                    print("Proszę wybrać liczbę z przedziału od 1 do 10!")
                break
            except ValueError:
                print("To nie jest liczba całkowita!")

        print("Mniam, mniam. Dziękuję.")
        self.hunger -= food_input
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun = 4):
        print("Hura!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

def main():
    crit_name = input("Jak chcesz nazwać swojego zwierzaka? ")
    crit = Critter(crit_name)

    choice = None  
    while choice != "0":
        print \
        ("""
        Opiekun zwierzaka
        0 - zakończ
        1 - słuchaj swojego zwierzaka
        2 - nakarm swojego zwierzaka
        3 - pobaw się ze swoim zwierzakiem
        """)
    
        choice = input("Wybierasz: ")
        print()

        # exit
        if choice == "0":
            print("Do widzenia.")

        # listen to your pet
        elif choice == "1":
            crit.talk()

        # feed your pet
        elif choice == "2":
            crit.eat()

        # play with your pet
        elif choice == "3":
            crit.play()
        
        elif choice == "stats":
            print(crit)

        # some unknown choice
        else:
            print("\nNiestety,", choice, "nie jest prawidłowym wyborem.")


main()
input("\n\nAby zakończyć program, naciśnij klawisz Enter.")