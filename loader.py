from data.seat import *
from data.worker import *

class Loader():
    def __init__(self):
        pass

    def translateIndex2Dto1D(i, j):
        return (i+1) * j

    def loadAdjacent(self, seatList, height, width):
        for h in range(height):
            for w in range(width):
                seatListIndex = translateIndex2Dto1D(h, w)
                adjacentSeats = []    
                if(h == 0):
                    bottomAdjacent = seatList[translateIndex2Dto1D(h+1, w)].type
                    if(w == 0):
                        rightAdjacent = seatList[translateIndex2Dto1D(h, w+1)].type
                        seatsList[seatListIndex].adjacent_seats = ['#', '#', rightAdjacent, bottomAdjacent]
                    elif(w == width-1):
                        leftAdjacent = seatList[translateIndex2Dto1D(h, w-1)].type
                        seatsList[seatListIndex].adjacent_seats = [leftAdjacent, '#', '#', bottomAdjacent]
                    else:
                        rightAdjacent = seatList[translateIndex2Dto1D(h, w+1)].type
                        leftAdjacent = seatList[translateIndex2Dto1D(h, w-1)].type
                        seatsList[seatListIndex].adjacent_seats = [leftAdjacent, '#', rightAdjacent, bottomAdjacent]
                elif(h == height-1):
                    topAdjacent = seatList[translateIndex2Dto1D(h-1, w)].type
                    if(h == height-1 and w == 0):
                        rightAdjacent = seatList[translateIndex2Dto1D(h, w+1)].type
                        seatsList[seatListIndex].adjacent_seats = ['#', topAdjacent, rightAdjacent, '#']
                    elif(h == height - 1 and w == width - 1):
                        leftAdjacent = seatList[translateIndex2Dto1D(h, w-1)].type
                        seatsList[seatListIndex].adjacent_seats = [leftAdjacent, topAdjacent, '#', '#']
                    else:
                        rightAdjacent = seatList[translateIndex2Dto1D(h, w+1)].type
                        leftAdjacent = seatList[translateIndex2Dto1D(h, w-1)].type
                        seatsList[seatListIndex].adjacent_seats = [leftAdjacent, topAdjacent, rightAdjacent, '#']
                elif(w==0):
                    topAdjacent = seatList[translateIndex2Dto1D(h-1, w)].type
                    rightAdjacent = seatList[translateIndex2Dto1D(h, w+1)].type
                    bottomAdjacent = seatList[translateIndex2Dto1D(h+1, w)].type
                    seatsList[seatListIndex].adjacent_seats = ['#', topAdjacent, rightAdjacent, bottomAdjacent]
                elif(w == width-1):
                    leftAdjacent = seatList[translateIndex2Dto1D(h, w-1)].type
                    topAdjacent = seatList[translateIndex2Dto1D(h-1, w)].type
                    bottomAdjacent = seatList[translateIndex2Dto1D(h+1, w)].type
                    seatsList[seatListIndex].adjacent_seats = [leftAdjacent, topAdjacent, '#', bottomAdjacent]
                else:
                    leftAdjacent = seatList[translateIndex2Dto1D(h, w-1)].type
                    topAdjacent = seatList[translateIndex2Dto1D(h-1, w)].type
                    rightAdjacent = seatList[translateIndex2Dto1D(h, w+1)].type
                    bottomAdjacent = seatList[translateIndex2Dto1D(h+1, w)].type
                    seatsList[seatListIndex].adjacent_seats = [leftAdjacent, topAdjacent, rightAdjacent, bottomAdjacent]

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
            
            loadAdjacent(seats, width, height)
            
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
                    skills.append(developer[3 + i])

                developers.append(Worker(company, 'D', potentialBonus, skills))

            ### PM PARSING ###
            line = fp.readline()
            numberOfPMs = int(line)

            for PM in range(numberOfPMs):
                line = fp.readline()
                PM = line.split()
                
                company = PM[0]
                potentialBonus = int(PM[1])

                projectManagers.append(Worker(company, 'P', potentialBonus))

        return (seats, developers + projectManagers)
        pass