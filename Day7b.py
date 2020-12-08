import re

def compile_rules(infile):
    bag_dict = {}
    out_bag = re.compile('^(\w+ \w+) bags contain')
    in_bag = re.compile('(\d+) (\w+ \w+) bag')
    with open(infile, 'r') as f:
        for row in f:
            rule = row.strip()
            if 'no other' not in rule:
                container = re.search(out_bag, rule)[1]
                bag_dict[container] = {y:int(x) for x,y in re.findall(in_bag, rule)}
    return bag_dict

def nested_rules(bag_rules, rule):
    inside_bags = 0
    if rule in bag_rules:
        for x,y in bag_rules[rule].items():
            inside_bags += y + (y * nested_rules(bag_rules, x))
    return inside_bags


if __name__ == '__main__':
    infile = 'Advent7.txt'
    bag_rules = compile_rules(infile)
    print(nested_rules(bag_rules, 'shiny gold'))
