
def best_friend_for_worker(worker, best_friends):
    # result = [(friend, fitness), ...]
    result = []
    for friend in best_friends:
        result.append((friend, fitness_w_w(worker, friend)))
    return reversed(sorted(result, key=lambda x: x[1]))

def best_worker_for_seat(seat, best_friends):
    result = []
    for worker, friends in best_friends:
        result.append((worker, fitness_s_w(seat, worker, friends)))
    return reversed(sorted(result, key=lambda x: x[1]))


def fitness_w_w(worker1, worker2):
    common_skills = [el for el in worker1.skills if el in worker2.skills]
    all_skills = [el for el in worker1.skills if el not in worker2.skills] + worker2.skills
    wp = len(common_skills) * len(all_skills)

    bp = worker1.bonus * worker2.bonus if worker1.company == worker2.company else 0

    return wp + bp

def fitness_s_w(seat, worker, best_friends):
    return 1