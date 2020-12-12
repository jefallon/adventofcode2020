cardinals = ['E', 'N', 'W', 'S']

def follow_path(infile):
    facing = 0
    location = [0,0]
    with open(infile, 'r') as f:
        for row in f:
            inst = row.strip()
            turn, hor, vert = follow_inst(inst, facing)
            facing += turn
            facing %= 4
            location[0] += hor
            location[1] += vert
    return abs(location[0])+abs(location[1])


def turn_right(degrees):
    turns = degrees//90
    steps = (0-turns)
    return steps

def turn_left(degrees):
    turns = degrees//90
    steps = turns
    return steps

def follow_inst(inst, facing):
    if inst[0] == 'R':
        return turn_right(int(inst[1:])), 0, 0
    if inst[0] == 'L':
        return turn_left(int(inst[1:])), 0, 0
    if inst[0] == 'N':
        return 0, 0, int(inst[1:])
    if inst[0] == 'S':
        return 0, 0, 0-int(inst[1:])
    if inst[0] == 'E':
        return 0, int(inst[1:]), 0
    if inst[0] == 'W':
        return 0, 0-int(inst[1:]), 0
    if inst[0] =='F':
        return follow_inst(cardinals[facing]+inst[1:], facing)

if __name__ == '__main__':
    infile = 'Advent12.txt'
    print(follow_path(infile))