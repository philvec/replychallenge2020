
class Worker:
    def __init__(self, company, role, bonus=0, skills=[], id=0):
        self.company = company
        self.role = role        # <--  {'D', 'P'}
        self.bonus = bonus
        self.skills = skills
        self.id = id
