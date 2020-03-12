from data.seat import *
from data.worker import *

filepaths = ['data/a_solar.txt', 'data/b_dream.txt', 'data/c_soup.txt', 'data/d_maelstrom.txt', 'data/e_igloos.txt', 'data/f_glitch.txt']

with open(filepaths[0]) as fp:
    ### MAP PARSING ###
    firstLine = fp.readline()
    width, height = firstLine.split()
    width = int(width)
    height = int(height)
    map = []

    for h in range(height):
        map.append([])
        mapLine = list(fp.readline())
        
        for w in range(width):
            map[h].append(Seat(w, h, mapLine[w]))
    
    ### DEVELOPER PARSING ###
    line = fp.readline()
    numberOfDevs = int(line)
    developers = []
    projectManagers = []

    for dev in range(numberOfDevs):
        line = fp.readline()
        developer = line.split()
        
        company = developer[0]
        potentialBonus = int(developer[1])
        numberOfSkills = int(developer[2])
        skills = []

        for i in range(numberOfSkills):
            skills.append(developer[2 + i])

        developers.append(Worker('D', potentialBonus, skills))

    ### PM PARSING ###
    line = fp.readline()
    numberOfPMs = int(line)

    for PM in range(numberOfPMs):
        line = fp.readline()
        PM = line.split()
        
        company = PM[0]
        potentialBonus = int(PM[1])

        projectManagers.append(Worker('P', potentialBonus))