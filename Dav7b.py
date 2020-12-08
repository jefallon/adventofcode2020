import re

def compile_rules(infile):
    bag_dict = {}
    out_bag = re.compile('^(\w+ \w+) bags contain')
    in_bag = re.compile('(\d+) (\w+ \w+) bag')
    with open(infile, 'r') as f:
        for row in f:
            rule = row.strip()
            if not rule.contains('no other'):
                container = re.search(out_bag, rule)[1]
                bags = {in_bag[2]: in_bag[1]}
                bag_dict[container] = bags
    return bag_dict

if __name__ == '__main__':
    infile = 'dummy7.txt'
    bag_rules = compile_rules(infile)
