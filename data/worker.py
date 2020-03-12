
class Worker:
    def __init__(self, role, bonus=0, skills=[]):
        self.role = role        # <--  {'D', 'P'}
        self.bonus = bonus
        self.skills = skills