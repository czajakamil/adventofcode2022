# Gra w karty 3.0

class Card():
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["c", "d", "h", "s"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def __str__(self):
        rep = self.rank + self.suit
        return rep

"""Karta, której ranga i kolor są nieznane"""
class Unprintable_Card(Card):
    def __str__(self):
        return "<utajniona>"

    """Karta, która może być odkryta lub zakryta"""
class Positionable_Card(Card):
    def __init__(self, rank, suit, face_up = True):
        """Wywołujemy konstruktor klasy nadrzędnej, aby ustawić atrybuty rank i suit."""
        super(Positionable_Card, self).__init__(rank, suit)
        self.is_face_up = face_up
    
    def __str__(self):
        if self.is_face_up:
            """Wywołujemy metodę __str__ klasy nadrzędnej, aby uzyskać reprezentację rangi i koloru karty."""
            rep = super(Positionable_Card, self).__str__()
        else:
            rep = "XX"
        return rep
    
    def flip(self):
        self.is_face_up = not self.is_face_up

# main
card1 = Card("A", "c")
card2 = Unprintable_Card("A", "d")
card3 = Positionable_Card("A", "h")
print("Wyświetlanie obiektu klasy Card:")
print(card1)
print("\nWyświetlanie obiektu klasy Unprintable_Card:")
print(card2)
print("\nWyświetlanie obiektu klasy Positionable_Card:")
print(card3)
print("Odwracanie stanu obiektu klasy Positionable_Card.")
card3.flip()
print("Odwrócony obiekt klasy Positionable_Card:")
print(card3)

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")