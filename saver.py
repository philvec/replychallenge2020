
def save(workers, best_workers, output_filename):
    output_dict = {}
    seats_taken = []
    av_seats = len([bw for bw in best_workers if bw[0].type !='#'])
    while(len(output_dict) < av_seats):
        for i, (seat, best_workers_for_seat) in enumerate(best_workers):
            if len(best_workers_for_seat) != 0:
                label = str(seat.x) + ' ' + str(seat.y)
                if best_workers_for_seat[0][1] > 0 and best_workers_for_seat[0][0].id not in output_dict and label not in seats_taken:
                    output_dict[best_workers_for_seat[0][0].id] = label
                    seats_taken.append(output_dict[best_workers_for_seat[0][0].id])
                best_workers[i] = (seat, best_workers_for_seat[1:])
        print(len(output_dict), av_seats)

    print(output_dict)
    output = [(output_dict[i] if i in output_dict else 'X') for i in range(len(workers))]
    with open(output_filename, 'w') as file_handle:
        for el in output:
            file_handle.write(el + '\n')