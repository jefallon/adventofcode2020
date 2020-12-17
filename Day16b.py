def read_rule(line):
    field, nums = line.strip().split(':')
    range_1, conj, range_2 = nums.strip().split()
    rule = {field: list(map(int, range_1.split('-'))) +
    list(map(int, range_2.split('-')))}
    return rule

def is_valid(ticket, rules):
    valid_keys = []
    for field_val in ticket:
        valid_fields = set()
        for x,y in rules.items():
            a,b,c,d = y
            if a <= field_val <=b or c <= field_val <= d:
                valid_fields.add(x)
        if valid_fields == set():
            return False
        valid_keys.append(valid_fields)
    return valid_keys

def name_fields(infile):
    data = 0
    rules = {}
    error_rate = 0
    with open(infile, 'r') as f:
        for line in f:
            if line.strip() == '':
                data += 1
                continue
            if data in [1,3]:
                if data == 1:
                    field_options = [set(rules.keys()) for _ in range(len(rules.keys()))]
                data += 1
                continue
            if data == 0:
                rules.update(read_rule(line))
            elif data == 2:
                my_ticket = list(map(int, line.strip().split(',')))
                for idx, fields in enumerate(is_valid(my_ticket, rules)):
                    field_options[idx].intersection_update(fields)
            elif data == 4:
                valid = is_valid(map(int, line.strip().split(',')), rules)
                if valid is not False:
                    for idx, fields in enumerate(valid):
                        field_options[idx].intersection_update(fields)
    return field_options, my_ticket

def unique_fields(field_options):
    field_positions = {}
    fields_found = 0
    ided_field = {}
    while fields_found < len(field_options):
        for i,j in enumerate(field_options):
            if len(j) == 1:
                field_positions[min(j)] = i
                ided_field = j
                fields_found += 1
                break
        field_options = [x.difference(ided_field) for x in field_options]
    return field_positions







if __name__ == '__main__':
    infile = 'Advent16.txt'
    field_options, my_ticket = name_fields(infile)
    field_indices = unique_fields(field_options)
    depart = 1
    for x,y in field_indices.items():
        if 'departure' in x:
            depart *= my_ticket[y]
    print(depart)