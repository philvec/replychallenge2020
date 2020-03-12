from loader import Loader
from fitness import best_friend_for_worker, best_worker_for_seat
from saver import save


filepaths = ['data/a_solar.txt', 'data/b_dream.txt', 'data/c_soup.txt', 'data/d_maelstrom.txt', 'data/e_igloos.txt', 'data/f_glitch.txt']

if __name__ == '__main__':
    loader = Loader()

    for file in filepaths:
        print('processing file ', file)
        seats, workers = loader.load(file)

        best_friends = []
        for i, worker in enumerate(workers):
            print('\r    calculating friends for worker ', i + 1, '/', len(workers), end='')
            best_friends.append((worker, best_friend_for_worker(worker, workers)))
        best_workers = []
        for i, seat in enumerate(seats):
            print('\r    calculating workers for seat ', i + 1, '/', len(seats), end='')
            best_workers.append((seat, best_worker_for_seat(seat, best_friends)))
        print('\r    Done kmining! Reorganising output...', end='')

        save(workers, best_workers, 'outputs/result_'+file.split('/')[-1])
        print('\r    Saved!')

        for w, f in best_friends:
            print(w.id, [(a.id, b) for (a, b) in f])
        print()
        for s, f in best_workers:
            print(s.x, s.y, [(a.id, b) for (a, b) in f])

