
if __name__ == '__main__':
    print('hello')


filepaths = ['data/a_solar.txt', 'data/b_dream.txt', 'data/c_soup.txt', 'data/d_maelstrom.txt', 'data/e_igloos.txt', 'data/f_glitch.txt']

with open(filepaths[0]) as fp:
    firstLine = fp.readline()
    width, height = firstLine.split()
    width = int(width)
    height = int(height)
    map = []

    for h in range(height):
        map.append([])
        mapLine = list(fp.readline())
        
        for w in range(width):
            map[h].append(mapLine[w])
    
    print(map)