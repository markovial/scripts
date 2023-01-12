import re
import os


def grades():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'data/grades.txt')

    with open(filename, "r") as file:
        grades = file.read()

    # pattern = "(.*)";
    # matches = re.findall(rf"{pattern}",grades)

    lines = grades.split('\n')
    lines.pop()
    bees = []
    #print(lines)
    #for _ in lines : print(_)
    for line in lines:
        words = line.split(' ')
    #    print(words)
        if (words[2] =='B'):
            temp = re.sub(":","",words[1])
            print(f"{ words[0] } { temp }")
            bees.append(f"{ words[0] } { temp }")

    # print(bees)
    print(len(bees))

grades()

