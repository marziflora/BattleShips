'''
Plik wyswietlacz umożliwia wyświetlenie planszy na podstawie zmiennej ships z pliku generator
Pole puste = _, pole ze statkiem = x

'''
import generator as g
import gracz as play

def show_board(ships, shot, attempt):
    g.board.clear()
    print("    A  B  C  D  E  F  G  H  I  J")
    for x in range(10):
        g.board.append(["_"] * 10)
    for row in range(0, 10):
        print(row +1, ' ', end="")
        if (row + 1 < 10):
            print(' ', end="")
        for column in range(0, 10):
            print(g.board[row][column],'', end=" ")
            for i, j in ships:
                g.board[i][j] = "x"
            for i, j in attempt:
                g.board[i][j] = "."
            for i, j in shot:
                g.board[i][j] = "S"
        print()


