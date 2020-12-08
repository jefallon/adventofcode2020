def find_acc(infile):
	with open(infile, 'r') as f:
		instruction_list = []
		for row in f:
			inst = row.strip().split()
			instruction_list.append([inst[0], int(inst[1])])
	next_inst = 0
	acc = 0
	seen = set()
	for i, test_val in enumerate(instruction_list):
		if test_val[0] == 'acc':
			continue
		instruction_list[i][0] = swap(test_val)
		while next_inst not in seen and next_inst < len(instruction_list):
			seen.add(next_inst)
			inst, shift = instruction_list[next_inst]
			if inst == 'nop':
				next_inst += 1
			elif inst == 'acc':
				acc += shift
				next_inst += 1
			elif inst == 'jmp':
				next_inst += shift
		if next_inst == len(instruction_list):
			return acc
		else:
			instruction_list[i][0] = swap(test_val)
			next_inst = 0
			acc = 0
			seen = set()

def swap(test_val):
	if test_val == 'nop':
		return 'jmp'
	elif test_val == 'jmp':
		return 'nop'



if __name__ == '__main__':
	infile = 'Advent8.txt'
	print(find_acc(infile))