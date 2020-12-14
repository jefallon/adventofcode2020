def get_buses(infile):
    with open(infile, 'r') as f:
        arrival = int(next(f).strip())
        buses = next(f).strip().split(',')
        in_service = [x for x in enumerate(buses) if x[1] != 'x']
        in_service = [(x,int(y)) for x,y in in_service]
        return in_service

def find_consecutive(buses):
    first_bus = buses[0][1]
    first_time = buses[0][0]
    while True:
        # print(first_time)
        for minutes, bus in buses[1:]:
            if (first_time + minutes) % bus:
                first_bus *= bus
                buses.remove((minutes, bus))
                # print(buses)
                # print(first_bus)
                # print(first_time)

                # print(bus)
                break
        else:
            return first_time
        first_time += first_bus

if __name__ == '__main__':
    # buses = get_buses('Advent13.txt')
    buses = [(0,17), (2,13), (3,19)]
    print(find_consecutive(buses))