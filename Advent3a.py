def countTrees(infile):
	trees = 0
	with open(infile, 'r') as f:
		horiz = 0
		for row in f:
			if row.strip()[horiz] == '#':
				trees += 1
			horiz += 3
			horiz %= 31
	return trees

if __name__ == '__main__':
	infile = 'Advent3.txt'
	print(countTrees(infile))