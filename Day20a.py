from itertools import combinations, permutations, product

def read_tiles(infile):
    tiles = {}
    labels = []
    with open(infile, 'r')  as f:
        for row in f:
            line = row.strip()
            if line == '':
                tile = None
            elif line[0] == 'T':
                tile = int(line.split()[1].split(':')[0])
                labels.append(tile)
                tiles[tile] = []
            else:
                tiles[tile].append(list(map(lambda x: '1' if x == '#' else '0', list(line))))
    return labels, tiles

def get_border(tile):
    top = int(''.join(tile[0]), base = 2)
    bottom = int(''.join(tile[-1]), base = 2)
    left = int(''.join(t[0] for t in tile), base = 2)
    right = int(''.join(t[-1] for t in tile), base = 2)
    return top, right, bottom, left

def flip(tile):
    return(tile[::-1])

def r90(tile):
    l = len(tile)
    rot = [[t[i] for t in tile[::-1]] for i in range(l)]
    return rot

def get_symmetries(tile):
    symm = [tile]
    for i in range(3):
        symm.append(r90(symm[-1]))
    symm.extend([flip(x) for x in symm])
    return symm

def get_dihedral_borders(tile):
    return [get_border(x) for x in get_symmetries(tile)]

def all_dihedral_borders(tiles):
    borders = {}
    for key, tile in tiles.items():
        borders[key] = get_dihedral_borders(tile)
    return borders

def find_neighbors(labels, dihedral_borders):
    neighbors = {tile: [[[] for _ in range(4)] for _ in range(8)] for tile in labels}
    for tile1, tile2 in combinations(labels, 2):
        for idx1, rot1 in enumerate(dihedral_borders[tile1]):
            for idx2, rot2 in enumerate(dihedral_borders[tile2]):
                for side in range(4):
                    if rot1[side] == rot2[(side+2)%4]:
                        neighbors[tile1][idx1][side].append({tile2:idx2})
                        neighbors[tile2][idx2][(side+2)%4].append({tile1:idx1})
    return neighbors

def check_bottom(tile, rot, seen =set()):
    above = 0
    col = [[tile, rot]]
    # seen.add(tile)
    seen ={tile}
    this = tile
    symm = rot
    while neighbors[this][symm][0] != []:
        up_neighbor, up_rot = list(neighbors[this][symm][0][0].items())[0]
        if up_neighbor in seen:
            break
        seen.add(up_neighbor)
        this = up_neighbor
        symm = up_rot
        col.append([this, symm])
        above += 1
    if above >= 11:
        return col


def check_left(tile, rot, seen = set()):
    right = 0
    row = [[tile, rot]]
    # seen.add(tile)
    seen ={tile}
    this = tile
    symm = rot
    while neighbors[this][symm][1] != []:
        r_neighbor, r_rot = list(neighbors[this][symm][1][0].items())[0]
        if r_neighbor in seen:
            break
        seen.add(r_neighbor)
        this = r_neighbor
        symm = r_rot
        row.append([this, symm])
        right += 1
    if right >= 11:
        return row

def find_bottom_left():
    for tile, rot in product(labels, range(8)):
        a = check_bottom(tile, rot)
        if a:
            b = check_left(tile, rot)
            if b:
                prod = tile
                prod *= a[-1][0]
                prod *= b[-1][0]
                prod *= check_bottom(b[-1][0], b[-1][1])[-1][0]
    return prod

if __name__ == '__main__':
    infile = 'Advent20.txt'
    labels, tiles = read_tiles(infile)
    dihedral_borders = all_dihedral_borders(tiles)
    neighbors = find_neighbors(labels, dihedral_borders)
    print(find_bottom_left())

