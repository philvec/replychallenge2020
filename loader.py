from data.seat import *
from data.worker import *

class Loader():
    def __init__(self):
        pass

    def load(self, file):
        # seats = []   <- list of Seat
        # workers = []  <- list of Worker
        # return (seats, workers)
        seats = []
        developers = []
        projectManagers = []

        with open(file) as fp:
            ### MAP PARSING ###
            firstLine = fp.readline()
            width, height = firstLine.split()
            width = int(width)
            height = int(height)

            for h in range(height):
                mapLine = list(fp.readline())
                
                for w in range(width):
                    seats.append(Seat(w, h, mapLine[w]))
            
            ### DEVELOPER PARSING ###
            line = fp.readline()
            numberOfDevs = int(line)

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

        return (seats, developers + projectManagers)