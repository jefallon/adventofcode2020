def groups_sum(infile):
    yes_sum = 0
    with open(infile, 'r') as f:
        this_group = set()
        for row in f:
            responses = row.strip()
            if responses == '':
                yes_sum += len(this_group)
                this_group = set()
            else:
                this_group.update(set(responses))
        yes_sum += len(this_group)
    return yes_sum

if __name__ == '__main__':
    infile= 'Advent6.txt'
    print(groups_sum(infile))
