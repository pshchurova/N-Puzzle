import sys
import random

def find_padding(max):
    i = 10
    res = 1
    while max / i >= 1:
        res += 1
        i *= 10
    return(res)

def createPuzzle(dim):
    tab = []
    for x in range(dim):
        tab += range(x * dim, (x+1) * dim)

    random.shuffle(tab)
    res = []
    for i in range(dim):
        res += [tab[i * dim: (i + 1) * dim]]
    return res

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.stderr.write("usage generator.py [dimension tile]\n")
        exit(1)
    try:
        dim = int(sys.argv[1])
        if dim >= 100 or dim <= 0:
            raise Exception("number should be between 1 and 99")
    except Exception as e:
        sys.stderr.write(str(e)+"\n")
        sys.stderr.write("usage generator.py x [dimension tile (0 < x < 100)]\n")
        exit(1)

    res = createPuzzle(dim)
    f = open('random.txt', "w+")
    padding = find_padding(dim * dim)
    f.write("## Randomly generated tile of dimension "+ str(dim) +" ##\n")
    f.write(str(dim))
    for x in range(dim):
        f.write(' '.join(str(e).ljust(padding) for e in res[x])+"\n")