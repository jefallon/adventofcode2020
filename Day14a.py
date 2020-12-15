def read_mask(str_mask):
    mask_vals = {}
    for idx, mask_bit in enumerate(str_mask[::-1]):
        if mask_bit != 'X':
            mask_vals[idx] = int(mask_bit)
    return mask_vals

def mask_val(raw_val, mask):
    output_val = raw_val
    for x,y in mask.items():
        if y == 0:
            output_val = ((output_val >> (x+1))<<(x+1)) + (output_val % (2**x))
        else:
            output_val |= 2**x
    return output_val



def get_vals(infile):
    address = {}
    with open(infile, 'r') as f:
        for row in f:
            x, y, z = row.strip().split()
            if x =='mask':
                mask = read_mask(z)
            else:
                to_mask =int(z)
                mem_key = x.split('[')[1][:-1]
                address[mem_key] = mask_val(to_mask, mask)
    return sum(address.values())

if __name__== '__main__':
    infile = 'Advent14.txt'
    print(get_vals(infile))