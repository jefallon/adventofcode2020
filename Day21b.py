def tidy_allergens(string):
    return set(string.replace('contains ', '').replace(')', '').split(', '))

def read_food(line):
    ingredients, allergens = line.strip().split(' (')
    ingredients = set(ingredients.split())
    allergens = tidy_allergens(allergens)
    return {allergen: ingredients for allergen in allergens}

def identify_allergies(infile):
    allergies = {}
    foods = set()
    canon = {}
    with open(infile, 'r') as f:
        for line in f:
            for allergen, ingredients in read_food(line).items():
                if allergen in allergies:
                    allergies[allergen] = allergies[allergen].intersection(ingredients)
                else:
                    allergies[allergen] = ingredients
                foods |= ingredients
    while allergies != {}:
        to_pop = set()
        for x,y in allergies.items():
            if len(y) == 1:
                to_pop.add(x)
            else:
                allergies[x] = {a for a in y if a in foods}
        for x in to_pop:
            y = allergies.pop(x)
            canon[x] = y
            foods.difference_update(y)
    return foods, allergies, canon

def get_canon_list(canon):
    return str([min(y) for x,y in sorted(canon.items())]).replace(' ', '')[1:-1]


if __name__ == '__main__':
    infile = 'Advent21.txt'
    foods, allergies, canon = identify_allergies(infile)
    clean_ingredients = 0
    with open(infile, 'r') as f:
        for row in f:
            for food in row.strip().split(' (')[0].split():
                if food in foods:
                    clean_ingredients += 1
    print(get_canon_list(canon))