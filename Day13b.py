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
        for minutes, bus in buses[1:]:
            if (first_time + minutes) % bus:
                break
            else:
                first_bus *= bus
                buses.remove((minutes, bus))
                break
        else:
            return first_time
        if len(buses) == 1:
            return(first_time)
        first_time += first_bus



if __name__ == '__main__':
    buses = get_buses('Advent13.txt')
    print(find_consecutive(buses))