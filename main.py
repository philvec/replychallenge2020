from loader import Loader
from fitness import best_friend_for_worker, best_worker_for_seat
from saver import save
from evaluate import score


filepaths = ['data/a_solar.txt', 'data/b_dream.txt', 'data/c_soup.txt', 'data/d_maelstrom.txt', 'data/e_igloos.txt', 'data/f_glitch.txt']
sizes = [(5, 3), (100, 100), (200, 200), (300, 200), (500, 400), (500, 400)]

if __name__ == '__main__':
    loader = Loader()

    for fi, file in enumerate(filepaths):
        print('processing file ', file)
        seats, workers = loader.load(file)
        seats = [seat for seat in seats if seat.type != "#"]

        best_friends = []
        for i, worker in enumerate(workers):
            print('\r    calculating friends for worker ', i + 1, '/', len(workers), end='')
            best_friends.append((worker, best_friend_for_worker(worker, workers)))
        best_workers = []
        for i, seat in enumerate(seats):
            print('\r    calculating workers for seat ', i + 1, '/', len(seats), end='')
            best_workers.append((seat, best_worker_for_seat(seat, best_friends)))
        print('\r    Done kmining! Reorganising output...', end='')

        best_workers = list(reversed(sorted(best_workers, key=lambda x: x[1][0][1])))

        output_dict = save(workers, best_workers, 'outputs/result_'+file.split('/')[-1])
        print('\r    Saved! score: ', end='')
        score = score(sizes[fi], output_dict, {worker.id: worker for worker in workers})
        print(score)

