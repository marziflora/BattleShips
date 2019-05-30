import battleship_generator as g
import matplotlib.pyplot as plt

g.generateships()
ships_500 = []

repeate = 1000
for i in range(0,repeate):
    g.generateships()
    ships_500 = ships_500 + g.ships

X = []
Y = []
for i in range(0,20*repeate):
    X.append(ships_500[i][0])
    Y.append(ships_500[i][1])

plt.scatter(X, Y, alpha=0.002, c="blue")
plt.show()

dict = {}
for i in range(0,repeate):
    try:
        dict[str(ships_500[i])] += 1
    except:
        dict[str(ships_500[i])] = 1

lists = sorted(dict.items()) # sorted by key, return a list of tuples
x, y = zip(*lists) # unpack a list of pairs into two tuples

plt.plot(x, y)
plt.title("Times of sampling depending on the position")
plt.xlabel("Position")
plt.tick_params(labelsize=10, labelrotation=90)
plt.ylabel("How many times the field was chosen")
plt.show()