# Gra w wojnę
"""Zasady gry:
1. Przetasowaną talię kart dzieli się na dwie części, rozdaje graczom i kładzie koszulkami do góry.
2. Pierwszy i drugi zawodnik równocześnie wykładają po jednej karcie i porównują ich wartości (względem starszeństwa, kolory nie odgrywają roli).
3. Gracz mający kartę o wyższej wartości odbiera karty i kładzie je pod spodem swojej talii.
4. Jeśli karty mają taką samą siłę (as na asa, król na króla, itp.), rozpętuje się wojna.
5. Należy odkryć po jednej karcie, położyć je koszulkami do góry na swoich kartach odkrytych, a następnie wyciągnąć następną kartę, położyć odkryte na zakrytych kartach i wówczas są one porównywane.
6. Karta o wyższej wartości wygrywa, a zwycięzca wojny odbiera wszystkie karty wykorzystane w wojnie.
7. Proces jest powtarzany, jeśli w okresie wojny znowu nie można wyłonić zwycięzcy.
8. Wygrywa ten, kto pierwszy zabierze wszystkie karty przeciwnikowi.
"""
import gry
def main():
    print("\t\tWitaj w grze w Wojnę!\n")

    names = []
    number = gry.ask_number("Podaj liczbę graczy (1 - 7): ", low=1, high=8)
    for i in range(number):
        name = input("Wprowadź nazwę gracza: ")
        names.append(name)
    print()

    game = W_Game(names)

    again = None
    while again != "n":
        game.play()
        again = gry.ask_yes_no("\nCzy chcesz zagrać ponownie?: ")

if __name__ == "__main__":
    main()