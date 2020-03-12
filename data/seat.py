
class Seat:
    def __init__(self, x, y, type='#', adjacent_seats=['#', '#', '#', '#']):
        self.x = x
        self.y = y
        self.type = type
        self.adjacent_seats = adjacent_seats
