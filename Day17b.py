def get_seed(infile):
    active_cells = set()
    with open(infile, 'r') as f:
        x = 0
        for row in f:
            for y, status in enumerate(list(row.strip())):
                if status == '#':
                    active_cells.add((x,y,0,0))
            x += 1
            y = len(row)
        dim_x = x
        dim_y = y
    return active_cells, dim_x, dim_y

def new_cycle(prev_cycle, cycle_no = 1):
    dim_x = prev_cycle[1]
    dim_y = prev_cycle[2]
    old_actives = prev_cycle[0]
    new_actives= set()
    for x in range(0-cycle_no-1, dim_x + 1):
        for y in range(0-cycle_no-1, dim_y + 1):
            for z in range(0-cycle_no, cycle_no + 1):
                for w in range(0-cycle_no, cycle_no + 1):
                    neighbors = get_neighbors(x,y,z,w)
                    active_neighbors = len(neighbors.intersection(old_actives))
                    if (x,y,z,w) in old_actives:
                        if active_neighbors in [2,3]:
                            new_actives.add((x,y,z,w))
                    elif  active_neighbors == 3:
                        new_actives.add((x,y,z,w))
    return new_actives, dim_x+2, dim_y+2


def get_neighbors(x,y,z,w):
    neighbors = set()
    dim_x = [x-1, x, x+1]
    dim_y = [y-1, y, y+1]
    dim_z = [z-1, z, z+1]
    dim_w = [w-1, w, w+1]
    for a in dim_x:
        for b in dim_y:
            for c in dim_z:
                for d in dim_w:
                    neighbors.add((a,b,c,d))
    neighbors.remove((x,y,z,w))
    return neighbors

def run_cycles(seed_cycle, cycles):
    old_cycle = seed_cycle
    for cycle in range(1, cycles+1):
        old_cycle = new_cycle(old_cycle, cycle)
    return old_cycle




if __name__ == '__main__':
    infile = 'Advent17.txt'
    seed_cycle = get_seed(infile)
    print(len(run_cycles(seed_cycle, 6)[0]))