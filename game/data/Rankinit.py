def rank_init():
    f = open('game/data/rank.txt', 'w')
    for i in range(9):
        f.write("None 0\n")
    f.write("None 0")

def self_init():
    f = open('rank.txt', 'w')
    for i in range(9):
        f.write("None 0\n")
    f.write("None 0")

self_init()