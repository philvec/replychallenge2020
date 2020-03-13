
def best_friend_for_worker(worker, best_friends):
    # result = [(friend, fitness), ...]
    result = []
    for friend in best_friends:
        if friend.id != worker.id:
            result.append((friend, fitness_w_w(worker, friend)))
    return list(reversed(sorted(result, key=lambda x: x[1])))

def best_worker_for_seat(seat, best_friends):
    result = []
    if seat.type == "#":
        return []
    for i, (worker, friends) in enumerate(best_friends):
        result.append((worker, fitness_s_w(seat, worker, friends)))
    return list(reversed(sorted(result, key=lambda x: x[1])))


def fitness_w_w(worker1, worker2):
    c_s = 0
    for skill in worker1.skills:
        if skill in worker2.skills:
            c_s += 1
    a_s = len(worker1.skills) + len(worker2.skills) - c_s
    wp = c_s * a_s

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

    while developers_counter < number_of_developers or project_managers_counter < number_of_project_managers and friends_counter < len(workers_friends):
        if workers_friends[friends_counter][0].role == '_':
            fitness += workers_friends[friends_counter][1]
            developers_counter += 1
        elif workers_friends[friends_counter][0].role == 'M':
            fitness += workers_friends[friends_counter][1]
            project_managers_counter += 1
        friends_counter += 1

    return fitness

