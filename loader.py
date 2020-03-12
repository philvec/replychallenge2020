from data.seat import *
from data.worker import *


def translateIndex2Dto1D(i, j, width):
    return width * i + j

def loadAdjacent(seatsList, height, width):
    for h in range(height):
        for w in range(width):
            seatsListIndex = translateIndex2Dto1D(h, w, width)
            adjacentSeats = []    
            if(h == 0):
                bottomAdjacent = seatsList[translateIndex2Dto1D(h+1, w, width)].type
                if(w == 0):
                    rightAdjacent = seatsList[translateIndex2Dto1D(h, w+1, width)].type
                    seatsList[seatsListIndex].adjacent_seats = ['#', '#', rightAdjacent, bottomAdjacent]
                elif(w == width-1):
                    leftAdjacent = seatsList[translateIndex2Dto1D(h, w-1, width)].type
                    seatsList[seatsListIndex].adjacent_seats = [leftAdjacent, '#', '#', bottomAdjacent]
                else:
                    rightAdjacent = seatsList[translateIndex2Dto1D(h, w+1, width)].type
                    leftAdjacent = seatsList[translateIndex2Dto1D(h, w-1, width)].type
                    seatsList[seatsListIndex].adjacent_seats = [leftAdjacent, '#', rightAdjacent, bottomAdjacent]
            elif(h == height-1):
                topAdjacent = seatsList[translateIndex2Dto1D(h-1, w, width)].type
                if(h == height-1 and w == 0):
                    rightAdjacent = seatsList[translateIndex2Dto1D(h, w+1, width)].type
                    seatsList[seatsListIndex].adjacent_seats = ['#', topAdjacent, rightAdjacent, '#']
                elif(h == height - 1 and w == width - 1):
                    leftAdjacent = seatsList[translateIndex2Dto1D(h, w-1, width)].type
                    seatsList[seatsListIndex].adjacent_seats = [leftAdjacent, topAdjacent, '#', '#']
                else:
                    rightAdjacent = seatsList[translateIndex2Dto1D(h, w+1, width)].type
                    leftAdjacent = seatsList[translateIndex2Dto1D(h, w-1, width)].type
                    seatsList[seatsListIndex].adjacent_seats = [leftAdjacent, topAdjacent, rightAdjacent, '#']
            elif(w==0):
                topAdjacent = seatsList[translateIndex2Dto1D(h-1, w, width)].type
                rightAdjacent = seatsList[translateIndex2Dto1D(h, w+1, width)].type
                bottomAdjacent = seatsList[translateIndex2Dto1D(h+1, w, width)].type
                seatsList[seatsListIndex].adjacent_seats = ['#', topAdjacent, rightAdjacent, bottomAdjacent]
            elif(w == width-1):
                leftAdjacent = seatsList[translateIndex2Dto1D(h, w-1, width)].type
                topAdjacent = seatsList[translateIndex2Dto1D(h-1, w, width)].type
                bottomAdjacent = seatsList[translateIndex2Dto1D(h+1, w, width)].type
                seatsList[seatsListIndex].adjacent_seats = [leftAdjacent, topAdjacent, '#', bottomAdjacent]
            else:
                leftAdjacent = seatsList[translateIndex2Dto1D(h, w-1, width)].type
                topAdjacent = seatsList[translateIndex2Dto1D(h-1, w, width)].type
                rightAdjacent = seatsList[translateIndex2Dto1D(h, w+1, width)].type
                bottomAdjacent = seatsList[translateIndex2Dto1D(h+1, w, width)].type
                seatsList[seatsListIndex].adjacent_seats = [leftAdjacent, topAdjacent, rightAdjacent, bottomAdjacent]
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
            
            loadAdjacent(seatsList=seats, height=height, width=width)
            
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

                developers.append(Worker(company, '_', potentialBonus, skills, dev))

            ### PM PARSING ###
            line = fp.readline()
            numberOfPMs = int(line)

            for PMnumber in range(numberOfPMs):
                line = fp.readline()
                PM = line.split()
                
                company = PM[0]
                potentialBonus = int(PM[1])

                projectManagers.append(Worker(company, 'M', potentialBonus, id=(numberOfDevs + PMnumber)))

        return (seats, developers + projectManagers)
        pass