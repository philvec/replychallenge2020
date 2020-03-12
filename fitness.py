
def best_friend_for_worker(worker, best_friends):
    # result = [(friend, fitness), ...]
    result = []
    for friend in best_friends:
        result.append((friend, 1.0))
    return result

def best_worker_for_seat(seat, best_friends):
    # result = [(worker, fitness), ...]
    result = []
    for worker, friends in best_friends:
        result.append((worker, 1.0))
    return result



def fitness_w_w(worker1, worker2):
    common_skills = [el for el in worker1.skills if el in worker2.skills]
    all_skills = [el for el in worker1.skills if el not in worker2.skills] + worker2.skills
    wp = len(common_skills) * len(all_skills)

    bp = worker1.bonus * worker2.bonus if worker1.company == worker2.company else 0

    return wp + bp

def fitness_s_w(seat, worker):
    return 1