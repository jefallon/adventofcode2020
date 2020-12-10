def find_weakness(infile):
	invalid_number = 90433990
	partial_sum = 0
	partial_summands = []
	with open(infile, 'r') as f:
		for row in f:
			summand = int(row.strip())
			partial_sum += summand
			partial_summands.append(summand)
			if partial_sum == invalid_number and len(partial_summands) > 1:
				return min(partial_summands) + max(partial_summands)
			while partial_sum > invalid_number:
				partial_sum -= partial_summands.pop(0)

				
if __name__ == '__main__':
	infile = 'Advent9.txt'
	print(find_weakness(infile))
