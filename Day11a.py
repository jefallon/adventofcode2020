def life_setup(infile):
    seats = []
    with open(infile, 'r') as f:
        for row in f:
            seats.append(list(row.strip()))
    seats = [['.']+row+['.'] for row in seats]
    dummy_row = ['.' for _ in range(len(seats[0]))]
    seats = [dummy_row]+seats+[dummy_row]
    return seats

def conway_step(seats):
    fill_seats = []
    empty_seats = []
    steps = [(x,y) for x in range(-1,2) for y in range(-1,2) if (x,y) !=(0,0)]
    for i in range(1,len(seats)-1):
        for j in range(1,len(seats[i])-1):
            visible_neighbors = []
            if seats[i][j] == 'L':
                for a, b in steps:
                    x, y = i+a, j+b
                    if seats[x][y] != '.':
                        visible_neighbors.append(seats[x][y])
                if visible_neighbors.count('#') == 0:
                    fill_seats.append((i,j))

            elif seats[i][j] == '#':
                for a,b in steps:
                    x, y = i + a, j + b
                    if seats[x][y] != '.':
                        visible_neighbors.append(seats[x][y])
                if visible_neighbors.count('#') >= 4:
                    empty_seats.append((i,j))
    return fill_seats, empty_seats

def conway_life(seats):
    fill, empty = conway_step(seats)
    while len(fill)+len(empty) > 0:
        for x,y in fill:
            seats[x][y] = '#'
        for x,y in empty:
            seats[x][y] = 'L'
        fill, empty = conway_step(seats)
    return sum([x.count('#') for x in seats])

if __name__ == '__main__':
    infile = 'Advent11.txt'
    seats = life_setup(infile)
    print(conway_life(seats))



