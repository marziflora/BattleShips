'''
Plik generator generuje zmienną ships, w której trzyma pozycje statków
W zmiennej forbidden przetrzymuje zakazane pozycje (wykorzystane + otoczenie statku)

'''
import random

# columns=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
# rows=[1,2,3,4,5,6,7,8,9,10]
board = []
ships=[] #pozycje statków do odgadywania
forbidden=[] #po każdym dodaniu statku generują się pozycje dookoła statku, w których napewno nie może być następnego statku

def battleship4():
    slope = random.randint(0,1) #pionowo czy poziomo
    column = random.randint(0,6)
    row = random.randint(0,6)
    field= [row, column]
    while field in forbidden:
        slope = random.randint(0, 1)
        column = random.randint(0, 6)
        row = random.randint(0, 6)
        field = [row, column]
    if slope == 0: #pionowo
        ships.append([row, column]) #zapisz pierwsze pole
        ships.append([row+1, column])
        ships.append([row+2, column])
        ships.append([row+3, column]) #dodawanie do zmiennej ships
        for i in range(row-1, row+5):
            for j in range(column-1, column+2):
                forbidden.append([i, j])
    if slope == 1: #poziomo
        ships.append([row, column]) #zapisz pola
        ships.append([row, column+1])
        ships.append([row, column+2])
        ships.append([row, column+3])
        for i in range(row - 1, row + 2):
            for j in range(column - 1, column + 5):
                forbidden.append([i, j])

def submarine3():
    slope = random.randint(0,1) #pionowo czy poziomo
    column = random.randint(0,7)
    row = random.randint(0,7)
    if slope == 0:
        fields = [ [row, column], [row+1, column], [row+2, column]]
    if slope == 1:
        fields = [ [row, column], [row, column+1], [row, column+2]]
    while any(field in forbidden for field in fields):
        slope = random.randint(0, 1)
        column = random.randint(0, 7)
        row = random.randint(0, 7)
        if slope == 0:
            fields = [[row, column], [row + 1, column], [row + 2, column]]
        if slope == 1:
            fields = [[row, column], [row, column + 1], [row, column + 2]]
    if slope == 0: #pionowo #rysowanie
        ships.append([row, column]) #zapisz pierwsze pole
        ships.append([row+1, column])
        ships.append([row+2, column])
        for i in range(row - 1, row + 4):
            for j in range(column - 1, column + 2):
                forbidden.append([i, j])
    if slope == 1: #poziomo
        ships.append([row, column]) #zapisz pola
        ships.append([row, column+1])
        ships.append([row, column+2])
        for i in range(row - 1, row + 2):
            for j in range(column - 1, column + 4):
                forbidden.append([i, j])

def destroyer2():
    slope = random.randint(0,1)
    column = random.randint(0,8)
    row = random.randint(0,8)
    if slope == 0:
        fields = [ [row, column], [row+1, column]]
    if slope == 1:
        fields = [ [row, column], [row, column+1]]
    while any(field in forbidden for field in fields):
        slope = random.randint(0, 1)
        column = random.randint(0, 8)
        row = random.randint(0, 8)
        if slope == 0:
            fields = [[row, column], [row + 1, column]]
        if slope == 1:
            fields = [[row, column], [row, column + 1]]
    if slope == 0: #pionowo
        ships.append([row, column]) #zapisz pierwsze pole
        ships.append([row+1, column])
        for i in range(row - 1, row + 3):
            for j in range(column - 1, column + 2):
                forbidden.append([i, j])
    if slope == 1: #poziomo
        ships.append([row, column]) #zapisz pola
        ships.append([row, column+1])
        for i in range(row - 1, row + 2):
            for j in range(column - 1, column + 3):
                forbidden.append([i, j])

def ones1():
    column = random.randint(0,9)
    row = random.randint(0,9)
    fields = [ [row, column]]
    while any(field in forbidden for field in fields):
        column = random.randint(0, 9)
        row = random.randint(0, 9)
        fields = [[row, column]]
    ships.append([row, column]) #zapisz pierwsze pole
    for i in range(row - 1, row + 2):
        for j in range(column - 1, column + 2):
            forbidden.append([i, j])

def generateships():
    board.clear()
    ships.clear()
    forbidden.clear()
    battleship4()
    submarine3()
    submarine3()
    destroyer2()
    destroyer2()
    destroyer2()
    ones1()
    ones1()
    ones1()
    ones1()