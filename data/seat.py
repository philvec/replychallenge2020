
class Seat:
    def __init__(self, x, y, type=0, adjacent_seats=[0, 0, 0, 0]):
        self.x = x
        self.y = y
        self.type = type         # <--  {0-no, 1-DEVseat, 2-PMseat}
        # [left, up, right, down]  <--  {0-no, 1-DEVseat, 2-PMseat}
        self.adjacent_seats = adjacent_seats
