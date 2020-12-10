def count_joltages():
	with open('Advent10.txt', 'r') as f:
		adapters = [0]
		for row in f:
			adapters.append(int(row.strip()))
		adapters.sort()
		ones = 0
		threes = 1
		for i, joltage in enumerate(adapters[1:]):
			offset = joltage - adapters[i]
			if offset == 1:
				ones += 1
			elif offset == 3:
				threes += 1
	return ones * threes

if __name__ == '__main__':
	print(count_joltages())