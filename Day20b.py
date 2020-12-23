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
    if above >= map_dim -1:
        return col

def check_top(tile, rot, seen =set()):
    below = 0
    col = [[tile, rot]]
    # seen.add(tile)
    seen ={tile}
    this = tile
    symm = rot
    while neighbors[this][symm][2] != []:
        dn_neighbor, dn_rot = list(neighbors[this][symm][2][0].items())[0]
        if dn_neighbor in seen:
            break
        seen.add(dn_neighbor)
        this = dn_neighbor
        symm = dn_rot
        col.append([this, symm])
        below += 1
    if below >= map_dim - 1:
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
    if right >= map_dim - 1:
        return row

def find_top_left():
    for tile, rot in product(labels, range(8)):
        a = check_top(tile, rot)
        if a:
            b = check_left(tile, rot)
            if b:
                return [check_left(x,y) for x,y in check_top(tile, rot)]


def find_bottom_left():
    for tile, rot in product(labels, range(8)):
        a = check_bottom(tile, rot)
        if a:
            b = check_left(tile, rot)
            if b:
                return [check_left(x,y) for x,y in check_bottom(tile, rot)]

def make_map():
    sea_map = []
    for row in find_top_left():
        row_tiles = [get_symmetries(tiles[tile])[rot] for tile,rot in row]
        row_tiles = [[''.join(tile_row[1:-1]) for tile_row in tile[1:-1]] for tile in row_tiles]
        for i in range(len(row_tiles[0])):
            sea_map.append(''.join(tile[i] for tile in row_tiles))
        # print(row_tiles)


    return sea_map

def find_monsters(all_maps):
    for sea_map in all_maps:
        monsters = 0
        for row in range(map_height-2):
            for col in range(map_width-19):
                for monster in range(3):
                    if int(sea_map[row+monster][col:col+20], base = 2)&sea_monster[monster] != sea_monster[monster]:
                        break
                else:
                    monsters += 1
        if monsters > 0:
            return monsters, sea_map

def count_swells(map):
    swells = 0
    for row in map:
        for col in row:
            if col == '1':
                swells += 1
    return swells




if __name__ == '__main__':
    infile = 'Advent20.txt'
    sea_monster = [0b00000000000000000010,0b10000110000110000111,0b01001001001001001000]
    labels, tiles = read_tiles(infile)
    map_dim = int(len(labels)**(0.5))
    tile_dim = len(tiles[labels[0]])
    dihedral_borders = all_dihedral_borders(tiles)
    neighbors = find_neighbors(labels, dihedral_borders)
    sea_map = make_map()
    all_maps = [list(''.join(x) for x in y) for y in get_symmetries(sea_map)]
    map_height = len(sea_map)
    map_width = len(sea_map[0])
    monsters, correct_map = find_monsters(all_maps)
    monster_swells = monsters*15
    print(count_swells(correct_map)-monster_swells)
