from functools import reduce
from operator import mul

def countTrees(infile):
	trees = [0,0,0,0,0]
	slopes = [1,3,5,7]
	skip = 0
	with open(infile, 'r') as f:
		horiz = [0,0,0,0,0]
		for row in f:
			treeline = row.strip()
			for i,spot in enumerate(horiz[:4]):
				if treeline[spot] == '#':
					trees[i] += 1
			horiz[i] += 3
			horiz[i] %= 31
			if not skip:
				if treeline[horiz[-1]] == '#':
					trees[-1] += 1
				horiz[-1] += 1
				horiz[-1] %= 31
			skip ^= 1

	return reduce(mul, trees)

if __name__ == '__main__':
	infile = 'Advent3.txt'
	print(countTrees(infile))