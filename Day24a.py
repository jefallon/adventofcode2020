import re

nbr = re.compile('se|sw|ne|nw|e|w')
tiles = {}

def take_step(step, row, col):
    if step == 'e':
        col += 1
    elif step == 'w':
        col -= 1
    elif step == 'nw':
        row += 1
    elif step == 'se':
        row -= 1
    elif step == 'ne':
        row += 1
        col += 1
    elif step == 'sw':
        row -= 1
        col -= 1
    return row, col

def follow_inst(inst):
    row = 0
    col = 0
    for step in re.findall(nbr, inst):
        row, col = take_step(step, row, col)
    return row, col

def flip_tile(row, col):
    tiles[(row, col)] = tiles.get((row, col), 0) ^ 1

if __name__ == '__main__':
    infile = 'Advent24.txt'
    with open(infile, 'r') as f:
        for row in f:
            tile = follow_inst(row.strip())
            flip_tile(tile[0], tile[1])
    print(sum(tiles.values()))