def get_addresses(address, mask):
    addresses = [address]
    for idx, mask_bit in enumerate(mask[::-1]):
        if mask_bit == '1':
            addresses = [a | (1<<idx) for a in addresses]
        elif mask_bit == 'X':
            addresses.extend([a^(1<<idx) for a in addresses])
    return addresses

def sum_values(infile):
    addresses = {}
    with open(infile, 'r') as f:
        for row in f:
            x, y, z = row.strip().split()
            if x == 'mask':
                mask = z
            else:
                z = int(z)
                address = int(x[4:-1])
                for a in get_addresses(address, mask):
                    addresses[a] = z
    return sum(addresses.values())

if __name__ == '__main__':
    infile = 'Advent14.txt'
    print(sum_values(infile))