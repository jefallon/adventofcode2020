import itertools

def read_rule(line):
    key, val = line.split(':')
    val = val.strip()
    if val[0] == '"':
        return {int(key):val[1]}
    else:
        for branch in val.split('|'):
            return {int(key):[[int(rule) for rule in\
                branch.strip().split()]\
                for branch in val.split('|')]}

def resolve_rules(rules, cache, i=0):
    if i in cache:
        return cache[i]
    rule = rules[i]
    if isinstance(rule, str):
        cache[i] = rule
        return rule
    out = []
    for option in rule:
        temp = [resolve_rules(rules, cache, next_i) for next_i in option]
        out.extend(''.join(x) for x in itertools.product(*temp))
    cache[i] = out
    return out

def make_rules_and_strings(infile):
    strings = set()
    rules = {}
    with open(infile, 'r') as f:
        for row in f:
            row = row.strip()
            if row != '':
                if row[0] in 'ab':
                    strings.add(row)
                else:
                    rules.update(read_rule(row))

    return rules, strings


if __name__ == '__main__':
    infile = 'Advent19.txt'
    rules, strings = make_rules_and_strings(infile)
    valid = set(resolve_rules(rules, {}))
    print(len(valid.intersection(strings)))