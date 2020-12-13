from math import ceil

def get_wait(bus, arrival):
    next_bus = ceil(arrival/bus)
    wait = (bus * next_bus) - arrival
    return wait

def shortest_wait(infile):
    with open(infile, 'r') as f:
        arrival = int(next(f).strip())
        buses = next(f).strip()
        in_service = list(map(int, [bus for bus in buses.split(',') if bus != 'x']))
        soonest_bus = min(in_service, key = lambda x: get_wait(x, arrival))
        return soonest_bus * get_wait(soonest_bus,arrival)

if __name__ == '__main__':
    infile = 'Advent13.txt'
    print(shortest_wait(infile))