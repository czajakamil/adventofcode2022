# Demontruje tworzenie modułów

class Player(object):
    """Uczestnik gry."""
    def __init__(self, name, score = 0):
        self.name = name
        self.score = score
        print("Utworzono gracza: " + self.name)

    def __str__(self):
        rep = self.name + "\t" + str(self.score)
        return rep

def ask_yes_no(question):
    """Zadaje pytanie, na które można odpowiedzieć tak lub nie."""
    response = None
    while response not in ("t", "n"):
        response = input(question).lower()
    return response

def ask_number(question: str, low: int, high: int):
    """Popros o podanie liczby z określonego zakresu."""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

if __name__ == "__main__":
    print("Uruchomiono ten moduł bezpośrednio (zamiast go zaimportować).")
    input("\n\nAby zakończyć program, naciśnij klawisz Enter.")