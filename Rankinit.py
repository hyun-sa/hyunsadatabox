def rank_init():
    f = open('rank.txt', 'w')
    for i in range(9):
        f.write("None 0\n")
    f.write("None 0")
