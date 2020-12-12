def follow_path(infile):
    waypoint = [10,1]
    ship = [0,0]
    with open(infile, 'r') as f:
        for row in f:
            inst = row.strip()
            action = row[0]
            dist = int(row[1:])
            if action == 'F':
                ship = move_ship(ship, waypoint,dist)
            else:
                waypoint = move_waypoint(waypoint, action, dist)
    return ship

def move_waypoint(wp, action, dist):
    waypoint = wp
    if action == 'N':
        waypoint[1] += dist
    elif action == 'S':
        waypoint[1] -= dist
    elif action == 'W':
        waypoint[0] -= dist
    elif action == 'E':
        waypoint[0] += dist
    elif action == 'L':
        for i in range(dist//90):
            waypoint = [-waypoint[1], waypoint[0]]
    elif action == 'R':
        for i in range(dist//90):
            waypoint = [waypoint[1], -waypoint[0]]
    return waypoint

def move_ship(ship, waypoint, dist):
    pos = ship
    for i in range(dist):
        for dim in range(2):
            pos[dim] += waypoint[dim]
    return pos

if __name__ =='__main__':
    infile = 'Advent12.txt'
    print(sum(abs(n) for n in follow_path(infile)))