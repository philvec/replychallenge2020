
def best_friend_for_worker(worker, friends):
    # result = [(friend, fitness), ...]
    return []

def best_worker_for_seat(seat, workers):
    # result = [(worker, fitness), ...]
    return []



def fitness_w_w(worker1, worker2):
    common_skills = [el for el in worker1.skills if el in worker2.skills]
    all_skills = [el for el in worker1.skills if el not in worker2.skills] + worker2.skills
    wp = len(common_skills) * len(all_skills)

    if worker1.company == worker2.company:
        bp = 0
    return wp + bp

def fitness_s_w(seat, worker):
    return 1