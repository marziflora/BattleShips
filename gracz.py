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

dictionary = {
    "A1":[0,0],
    "A2":[1,0],
    "A3":[2,0],
    "A4":[3,0],
    "A5":[4,0],
    "A6":[5,0],
    "A7":[6,0],
    "A8":[7,0],
    "A9":[8,0],
    "A10":[9,0],
    "B1":[0,1],
    "B2": [1, 1],
    "B3": [2, 1],
    "B4": [3, 1],
    "B5": [4, 1],
    "B6": [5, 1],
    "B7": [6, 1],
    "B8": [7, 1],
    "B9": [8, 1],
    "B10": [9, 1],
    "C1": [0, 2],
    "C2": [1, 2],
    "C3": [2, 2],
    "C4": [3, 2],
    "C5": [4, 2],
    "C6": [5, 2],
    "C7": [6, 2],
    "C8": [7, 2],
    "C9": [8, 2],
    "C10": [9, 2],
    "D1": [0, 3],
    "D2": [1, 3],
    "D3": [2, 3],
    "D4": [3, 3],
    "D5": [4, 3],
    "D6": [5, 3],
    "D7": [6, 3],
    "D8": [7, 3],
    "D9": [8, 3],
    "D10": [9, 3],
    "E1": [0, 4],
    "E2": [1, 4],
    "E3": [2, 4],
    "E4": [3, 4],
    "E5": [4, 4],
    "E6": [5, 4],
    "E7": [6, 4],
    "E8": [7, 4],
    "E9": [8, 4],
    "E10": [9, 4],
    "F1": [0, 5],
    "F2": [1, 5],
    "F3": [2, 5],
    "F4": [3, 5],
    "F5": [4, 5],
    "F6": [5, 5],
    "F7": [6, 5],
    "F8": [7, 5],
    "F9": [8, 5],
    "F10": [9, 5],
    "G1": [0, 6],
    "G2": [1, 6],
    "G3": [2, 6],
    "G4": [3, 6],
    "G5": [4, 6],
    "G6": [5, 6],
    "G7": [6, 6],
    "G8": [7, 6],
    "G9": [8, 6],
    "G10": [9, 6],
    "H1": [0, 7],
    "H2": [1, 7],
    "H3": [2, 7],
    "H4": [3, 7],
    "H5": [4, 7],
    "H6": [5, 7],
    "H7": [6, 7],
    "H8": [7, 7],
    "H9": [8, 7],
    "H10": [9, 7],
    "I1": [0, 8],
    "I2": [1, 8],
    "I3": [2, 8],
    "I4": [3, 8],
    "I5": [4, 8],
    "I6": [5, 8],
    "I7": [6, 8],
    "I8": [7, 8],
    "I9": [8, 8],
    "I10": [9, 8],
    "J1": [0, 8],
    "J2": [1, 9],
    "J3": [2, 9],
    "J4": [3, 9],
    "J5": [4, 9],
    "J6": [5, 9],
    "J7": [6, 9],
    "J8": [7, 9],
    "J9": [8, 9],
    "J10": [9, 9]
}

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
    while len(first_player_ships_shot) !=20 and len(second_player_ships_shot) != 20:
        change = input("Tura pierwszego gracza. Jak będzie gotowy, niech wpisze G\n")
        while change != "G":
            print("Podano nieprawidłowy znak")
            change = input("Tura pierwszego gracza. Jak będzie gotowy, niech wpisze G\n")
        print("     Gracz pierwszy: \n Twoja plansza statków: \n")
        w.show_board(first_player_ships)
        shoot(second_player_ships, second_player_ships_shot, first_player_attempt)
        change = input("Tura drugiego gracza. Jak będzie gotowy, niech wpisze G\n")
        while change != "G":
            print("Podano nieprawidłowy znak")
            change = input("Zawołaj drugiego gracza. Jak będzie gotowy, niech wpisze G\n")
        if change == "G":
            print("     Gracz drugi: \n Twoja plansza statków: \n")
            w.show_board(second_player_ships)
            shoot(first_player_ships, first_player_ships_shot, second_player_attempt)
