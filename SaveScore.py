import fileinput
import sys

def save_new_score(newscore, newname):
    newscore = str(newscore)
    newname = str(newname)
    contained = 0
    linecount = 0
    for line in fileinput.input('rank.txt', inplace=True):
        name, score = line.split(' ')
        if int(score) < int(newscore) and contained == 0:
            line = line.replace(line, newname + " " + newscore + "\n" + line)
            contained = 1
        linecount += 1
        if linecount+contained < 11:
            sys.stdout.write(line)

        else:
            break
