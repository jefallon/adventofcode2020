def find_invalid_sum(infile):
	pre_sums = []
	seeds = []
	with open(infile, 'r') as f:
		for row in f:
			next_val = int(row.strip())
			if len(pre_sums) < 24:
				if len(seeds) > 1:
					pre_sums.append([next_val + s for s in seeds])
				seeds.append(next_val)
			else:
				for p in pre_sums:
					if next_val in p:
						break
				else:
					return next_val
				old_seed = seeds.pop(0)
				old_sums = pre_sums.pop(0)
				pre_sums.append([next_val + s for s in seeds])
				seeds.append(next_val)

if __name__ == '__main__':
	infile = 'Advent9.txt'
	print(find_invalid_sum(infile))