def read_rule(line):
    field, nums = line.strip().split(':')
    range_1, conj, range_2 = nums.strip().split()
    rule = {field: list(map(int, range_1.split('-'))) +
    list(map(int, range_2.split('-')))}
    return rule

def is_valid(ticket, rules):
    bad_vals = 0
    for field_val in ticket:
        for x,y in rules.items():
            a,b,c,d = y
            if a <= field_val <=b or c <= field_val <= d:
                break
        else:
            bad_vals += field_val
    return bad_vals

def count_valid(infile):
    data = 0
    rules = {}
    error_rate = 0
    with open(infile, 'r') as f:
        for line in f:
            if line.strip() == '':
                data += 1
                continue
            if data in [1,3]:
                data += 1
                continue
            if data == 0:
                print(read_rule(line))
                rules.update(read_rule(line))
            elif data >= 1:
                error_rate += is_valid(map(int, line.strip().split(',')), rules)
    return error_rate

if __name__ == '__main__':
    infile = 'Advent16.txt'
    print(count_valid(infile))