# Od 1 do 7 graczy współzawodniczy z rozdającym

import karty, gry

class BJ_Card(karty.Card):
    """Karta do gry w Blackjacka."""
    ACE_VALUE = 1
    
    """Zwraca liczbę z zakresu 1 do 10, zgodnie z wartością karty."""
    @property
    def value(self):
        if self.is_face_up:
            """Biorę indeks karty z klasy nadrzędnej i dodaję 1, aby uzyskać wartość karty"""
            value = BJ_Card.RANKS.index(self.rank) + 1
            """Dla waletów, dam i król wartość wynosi 10"""
            if value > 10:
                value = 10
        else:
            value = None
        return value

class BJ_Deck(karty.Deck):
    """Talia kart do gry w Blackjacka."""
    def populate(self):
        """SUITES i RANKS są już zdefiniowane w klasie nadrzędnej"""
        for suit in BJ_Card.SUITS:
            for rank in BJ_Card.RANKS:
                self.cards.append(BJ_Card(rank, suit))

class BJ_Hand(karty.Hand):
    """Ręka - karty trzymane przez gracza w trakcie gry."""
    def __init__(self, name):
        super(BJ_Hand, self).__init__()
        self.name = name

    """Zwraca wartość ręki dla gracza"""
    def __str__(self):
        rep = self.name + ":\t" + super(BJ_Hand, self).__str__()
        if self.total:
            rep += "(" + str(self.total) + ")"
        return rep

    @property
    def total(self) -> int:
        """Jeśli karta w ręce ma wartość None, to i cała ręka ma wartość None."""
        for card in self.cards:
            if not card.value:
                return None

        """Sumuj wartości kart, traktując każdego asa jako 1"""
        t = 0
        for card in self.cards:
            t += card.value

        """Ustal, czy ręka zawiera asa"""
        contains_ace = False
        for card in self.cards:
            if card.value == BJ_Card.ACE_VALUE:
                contains_ace = True

        """Jeśli ręka zawiera asa, a suma jest wystarczająco niska, można traktować asa jako 11"""
        if contains_ace and t <= 11:
            """Dodaj tylko 10, ponieważ już dodaliśmy 1 za asa"""
            t += 10

        return t

    def is_busted(self) -> bool:
        # Zwraca True, jeśli ręka przekroczyła 21
        return self.total > 21


class BJ_Player(BJ_Hand):
    """Gracz w Blackjacku."""
    def is_hitting(self) -> bool:
        response = gry.ask_yes_no("\t" + self.name + ", chcesz dobrać kartę? (T/N): ")
        return response == "t"

    def bust(self) -> None:
        print(self.name, "przekroczył.")
        self.lose()

    def lose(self) -> None:
        print(self.name, "przegrał.")

    def win(self) -> None:
        print(self.name, "wygrał.")

    def push(self) -> None:
        print(self.name, "remisuje.")

class BJ_Dealer(BJ_Hand):
    """Rozdający w grze Blackjack."""
    def is_hitting(self) -> bool:
        return self.total < 17

    def bust(self) -> None:
        print(self.name, "przekroczył.")

    def flip_first_card(self) -> None:
        first_card = self.cards[0]
        first_card.flip()

class BJ_Game(object):
    """Gra w Blackjacka."""
    def __init__(self, names):
        self.players = []
        for name in names:
            player = BJ_Player(name)
            self.players.append(player)

        self.dealer = BJ_Dealer("Rozdający")

        self.deck = BJ_Deck()
        self.deck.populate()
        self.deck.shuffle()

    @property
    def still_playing(self) -> list:
        sp = []
        for player in self.players:
            if not player.is_busted():
                sp.append(player)
        return sp

    def __additional_cards(self, player) -> None:
        while not player.is_busted() and player.is_hitting():
            self.deck.deal([player])
            print(player)
            if player.is_busted():
                player.bust()

    def play(self) -> None:
        """Rozdaj każdemu początkowe dwie karty."""
        self.deck.deal(self.players + [self.dealer], per_hand=2)
        self.dealer.flip_first_card() # ukryj pierwszą kartę rozdającego
        for player in self.players:
            print(player)
        print(self.dealer)

        # Rozdaj dodatkowe karty graczy.
        for player in self.players:
            self.__additional_cards(player)

        self.dealer.flip_first_card() # odsłoń pierwszą kartę rozdającego

        if not self.still_playing:
            # Wszyscy gracze przekroczyli 21, odsłoń drugą kartę rozdającego.
            print(self.dealer)
        else:
            # Daj dodatkowe karty rozdającemu.
            print(self.dealer)
            self.__additional_cards(self.dealer)

            if self.dealer.is_busted():
                # Wygrywa każdy, kto jeszcze pozostaje w grze.
                for player in self.still_playing:
                    player.win()
            else:
                # Porównaj punkty każdego gracza pozostającego w grze z punktami rozdającego.
                for player in self.still_playing:
                    if player.total > self.dealer.total:
                        player.win()
                    elif player.total < self.dealer.total:
                        player.lose()
                    else:
                        player.push()

        # Usuń karty wszystkich graczy.
        for player in self.players:
            player.clear()
        self.dealer.clear()

def main():
    print("\t\tWitaj w grze Blackjack!\n")

    names = []
    number = gry.ask_number("Podaj liczbę graczy (1 - 7): ", low=1, high=8)
    for i in range(number):
        name = input("Wprowadź nazwę gracza: ")
        names.append(name)
    print()

    game = BJ_Game(names)

    again = None
    while again != "n":
        game.play()
        again = gry.ask_yes_no("\nCzy chcesz zagrać ponownie?: ")

if __name__ == "__main__":
    main()