import generator as g
import wyswietlacz as w
import sys

ships_shot = []
first_player_ships_shot = [] #zbiera dane o polach, które zostały trafione
second_player_ships_shot = []
first_player_attempt = [] #zbiera wszystkie pola, które gracz wypróbował
second_player_attempt = []
first_player_ships = [] #statki 1 gracza
second_player_ships = [] #statki 2 gracza

letters = [chr(x).upper() for x in range(97, 107)]
numbers = [i for i in range(1,11)]

dictionary = {}
for i in range(len(letters)):
    for j in range(len(numbers)):
        dictionary[str(str(letters[i])+str(numbers[j]))] = [j,i] #utworzenie słownika konwertującego A1 --> 0,0 


def shoot(ships, ships_shot, guess):
    try:
        shoot_place = input("Podaj pole, które chcesz zestrzelić u przeciwnika: (np. A1)\n")
        shoot_place = dictionary[shoot_place]
        while shoot_place in guess:
            print("Już tam strzelałeś")
            shoot_place = input("Podaj pole, które chcesz zestrzelić u przeciwnika: (np. A1)\n")
            shoot_place = dictionary[shoot_place]
        guess.append(shoot_place)
        if shoot_place not in ships:
            print("Nie trafione")
        if shoot_place in ships:
            print("Trafione!")
            ships_shot.append(shoot_place)
    except:
        print("Podano nie poprawne pole")
        shoot(ships, ships_shot, guess)
    if len(ships_shot) == 20:
        print("Gratuluje, gracz wygrał grę")
        sys.exit(0)

if __name__ == "__main__":
    g.generateships()
    first_player_ships = g.ships[:]
    g.generateships()
    second_player_ships = g.ships[:]
    print("        BattleShip\n")
    print("Oznaczenia: \n _ puste pole \n S zestrzelony statek\n . pudło \n  ")
    while len(first_player_ships_shot) !=20 and len(second_player_ships_shot) != 20:
        change = input("Tura pierwszego gracza. Jak będzie gotowy, niech wpisze G1\n")
        while change != "G1":
            print("Podano nieprawidłowy znak")
            change = input("Tura pierwszego gracza. Jak będzie gotowy, niech wpisze G\n")
        print("     Gracz pierwszy: \n Twoja plansza statków: \n")
        w.show_board(first_player_ships, first_player_ships_shot, first_player_attempt)
        print("     Plansza przeciwnika: \n")
        w.show_board([], second_player_ships_shot, second_player_attempt) #przeciwnika
        shoot(second_player_ships, second_player_ships_shot, second_player_attempt)
        change = input("Tura drugiego gracza. Jak będzie gotowy, niech wpisze G2\n")
        while change != "G2":
            print("Podano nieprawidłowy znak")
            change = input("Zawołaj drugiego gracza. Jak będzie gotowy, niech wpisze G\n")
        print("     Gracz drugi: \n Twoja plansza statków: \n")
        w.show_board(second_player_ships, second_player_ships_shot, second_player_attempt)
        print("     Plansza przeciwnika: \n")
        w.show_board([], first_player_ships_shot, first_player_attempt)  #przeciwnika
        shoot(first_player_ships, first_player_ships_shot, first_player_attempt)
