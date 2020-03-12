
def save(workers, best_workers, output_filename):
    output = {}
    print(best_workers)
    all_empty = False
    while(not all_empty):
        all_empty = True
        for i, (seat, best_workers_for_seat) in enumerate(best_workers):
            if len(best_workers_for_seat) == 0:
                continue
            else:
                if best_workers_for_seat[0] not in output:
                    output[best_workers_for_seat[0].id] = str(best_workers_for_seat[0].X + ' ' + best_workers_for_seat[0].Y)
                best_workers[i] = (seat, best_workers_for_seat[1:])
                all_empty = False

    with open(output_filename, 'a') as file_handle:
        for key in output:
            file_handle.write(output[key] + '\n')