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

def resolve_loops(rules):
    cache = {}
    r_31 = set(resolve_rules(rules, cache, 31))
    r_42 = set(resolve_rules(rules, cache, 42))
    len_31 = {len(x) for x in r_31}
    len_42 = {len(x) for x in r_42}
    len_both = len_31.union(len_42)
    assert len(len_both) == 1
    word_len = len_both.pop()

    sum_valid = 0
    for s in strings:
        words = [s[0+i:word_len+i] for i in range(0, len(s), word_len)]
        n_words = len(words)

        n_31 = 0
        for word in reversed(words):
            if word in r_31:
                n_31 += 1
            else:
                break
        if 0 < n_31 < n_words/2 and all(word in r_42 for word in words[:-n_31]):
            sum_valid += 1

    return sum_valid

if __name__ == '__main__':
    infile = 'Advent19.txt'
    rules, strings = make_rules_and_strings(infile)
    rules[8] = [[42], [42, 8]]
    rules[11] = [[42, 31], [42, 11, 31]]
    valid = resolve_loops(rules)
    print(valid)