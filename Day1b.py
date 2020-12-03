from itertools import combinations

def c2(inFile, target = 2020):
    items = []
    with open(inFile, 'r') as f:
        for line in f.readlines():
            item = int(line.strip())
            items.append(item)
    items.sort() # put items increasing order so we can break
    item_set = set(items) # for faster lookup

    for i, item1 in enumerate(items):
        for item2 in items[i+1:]:
            remaining = target - (item1 + item2)
            if remaining in item_set:
                return (item1 * item2 * remaining)
            if remaining <= 0:
                break

if __name__ =='__main__':
    infile = 'Advent1.txt'
    print(c2(infile))