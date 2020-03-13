from fitness import fitness_w_w
import numpy as np
from loader import Loader


def score(size, output_dict, workers_dict):
    map = -1 * np.ones(size)

    for id in output_dict:
        x, y = output_dict[id]
        map[x, y] = id

    score = 0
    for x in range(map.shape[0]):
        for y in range(map.shape[1]):
            if map[x, y] >= 0:
                if x-1 >= 0 and map[x-1, y] >= 0:
                    score += fitness_w_w(workers_dict[map[x, y]], workers_dict[map[x-1, y]])
                if x+1 < map.shape[0] and map[x+1, y] >= 0:
                    score += fitness_w_w(workers_dict[map[x, y]], workers_dict[map[x+1, y]])
                if y-1 >= 0 and map[x, y-1] >= 0:
                    score += fitness_w_w(workers_dict[map[x, y]], workers_dict[map[x, y-1]])
                if y+1 < map.shape[1] and map[x, y+1] >= 0:
                    score += fitness_w_w(workers_dict[map[x, y]], workers_dict[map[x, y+1]])
    return score / 2.0

filepaths = ['data/a_solar.txt', 'data/b_dream.txt', 'data/c_soup.txt', 'data/d_maelstrom.txt', 'data/e_igloos.txt', 'data/f_glitch.txt']
sizes = [(5, 3), (100, 100), (200, 200), (300, 200), (500, 400), (500, 400)]

if __name__ == '__main__':
    loader = Loader()
    total_score = 0
    for fi, file in enumerate(filepaths):
        print('evaluating file ', file)
        _, workers = loader.load(file)

        output_dict = {}
        with open('outputs/result_'+file.split('/')[-1]) as f:
            for i, line in enumerate(f):
                parts = line.split(' ')
                if len(parts) == 2:
                    x, y = int(parts[0]), int(parts[1])
                    output_dict[i] = (x, y)

        sc = score(sizes[fi], output_dict, {worker.id: worker for worker in workers})
        total_score += sc
        print('    score: ', sc)

    print('TOTAL SCORE: ', total_score)

