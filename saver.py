
def save(workers, best_workers, output_filename):
    output = {}
    print(best_workers)
    for i, (seat, best_workers_for_seat) in enumerate(best_workers):
        if len(best_workers_for_seat) != 0:
            if best_workers_for_seat[0] not in output:
                output[best_workers_for_seat[0][0].id] = str(seat.x) + ' ' + str(seat.y)
            best_workers[i] = (seat, best_workers_for_seat[1:])

    with open(output_filename, 'a') as file_handle:
        for key in output:
            file_handle.write(output[key] + '\n')