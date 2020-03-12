
def best_friend_for_worker(worker, best_friends):
    # result = [(friend, fitness), ...]
    result = []
    for friend in best_friends:
        if friend.id != worker.id:
            result.append((friend, fitness_w_w(worker, friend)))
    return list(reversed(sorted(result, key=lambda x: x[1])))

def best_worker_for_seat(seat, best_friends):
    result = []
    for worker, friends in best_friends:
        result.append((worker, fitness_s_w(seat, worker, friends)))
    return list(reversed(sorted(result, key=lambda x: x[1])))


def fitness_w_w(worker1, worker2):
    common_skills = [el for el in worker1.skills if el in worker2.skills]
    all_skills = [el for el in worker1.skills if el not in worker2.skills] + worker2.skills
    wp = len(common_skills) * len(all_skills)

    bp = worker1.bonus * worker2.bonus if worker1.company == worker2.company else 0

    return wp + bp

def fitness_s_w(seat, worker, workers_friends):
    if worker.role != seat.type:
        return 0
    fitness = 0
    developers_counter = 0
    project_managers_counter = 0
    friends_counter = 0
    number_of_developers = seat.adjacent_seats.count('_')
    number_of_project_managers = seat.adjacent_seats.count('M')

    while project_managers_counter != number_of_project_managers and friends_counter < len(workers_friends):
        if workers_friends[friends_counter][0].role == 'M':
            fitness += workers_friends[friends_counter][1]
        friends_counter += 1

    friends_counter = 0
    while developers_counter != number_of_developers and friends_counter < len(workers_friends):
        if workers_friends[friends_counter][0].role == '_':
            fitness += workers_friends[friends_counter][1]
        friends_counter += 1

    return fitness

