
def save(workers, best_workers, output_filename):
    output_dict = {}
    for i, (seat, best_workers_for_seat) in enumerate(best_workers):
        if len(best_workers_for_seat) != 0:
            if best_workers_for_seat[0][0].id not in output_dict:
                output_dict[best_workers_for_seat[0][0].id] = str(seat.x) + ' ' + str(seat.y)
            best_workers[i] = (seat, best_workers_for_seat[1:])

    output = [(output_dict[i] if i in output_dict else 'X') for i in range(len(workers))]
    with open(output_filename, 'a') as file_handle:
        for el in output:
            file_handle.write(el + '\n')