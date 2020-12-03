from functools import reduce
from operator import mul


def countTrees(infile):
	trees = [0,0,0,0,0]
	slopes = [1,3,5,7]
	skip = 0
	horiz = [0,0,0,0,0]
	with open(infile, 'r') as f:
		for row in f:
			treeline = row.strip()
			for i,spot in enumerate(horiz[:4]):
				if treeline[spot] == '#':
					trees[i] += 1
				horiz[i] += slopes[i]
				horiz[i] %= 31
			if skip == 0:
				if treeline[horiz[4]] == '#':
					trees[4] += 1
			else:
				horiz[4] += 1
				horiz[4] %= 31
			skip ^= 1

	return reduce(mul, trees)

if __name__ == '__main__':
	infile = 'Advent3.txt'
	print(countTrees(infile))