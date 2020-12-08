import re

def compile_rules(infile):
    bag_dict = {}
    out_bag = re.compile('^(\w+ \w+) bags contain')
    in_bag = re.compile('\d+ (\w+ \w+) bag')
    with open(infile, 'r') as f:
        for row in f:
            rule = row.strip()
            container = re.search(out_bag, rule)[1]
            for bag in re.findall(in_bag, rule):
                if bag in bag_dict:
                    bag_dict[bag].update({container})
                else:
                    bag_dict[bag] = {container}
    return bag_dict

def update_nest(contain_set, bag_dict):
    new_contain = set()
    for bag in contain_set:
        try:
            new_contain.update(bag_dict[bag])
        except:
            pass
    new_contain.update(contain_set)
    if new_contain != contain_set:
        return update_nest(new_contain, bag_dict)
    return contain_set

if __name__ == '__main__':
    infile = 'Advent7.txt'
    bag_rules = compile_rules(infile)
    containing_bags = update_nest({'shiny gold'}, bag_rules)
    print(len(containing_bags) - 1)