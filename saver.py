
def save(workers, best_workers, output_filename):
    output_dict = {}
    seats_taken = []
    av_seats = len([bw for bw in best_workers if bw[0].type !='#'])
    print()
    all_taken = False
    while(len(output_dict) < av_seats and not all_taken):
        all_taken = True
        print('\r', len(output_dict), '-', av_seats, ' ...', end='')
        for i, (seat, best_workers_for_seat) in enumerate(best_workers):
            if len(best_workers_for_seat) != 0:
                label = str(seat.x) + ' ' + str(seat.y)
                if best_workers_for_seat[0][1] > 0 and best_workers_for_seat[0][0].id not in output_dict and label not in seats_taken:
                    output_dict[best_workers_for_seat[0][0].id] = (seat.x, seat.y)
                    seats_taken.append(label)
                best_workers[i] = (seat, best_workers_for_seat[1:])
                all_taken = False

    output = [(output_dict[i] if i in output_dict else None) for i in range(len(workers))]
    with open(output_filename, 'w') as file_handle:
        for el in output:
            file_handle.write((str(el[0]) + " " + str(el[1]) + '\n') if el is not None else "X\n")

    return output_dict
