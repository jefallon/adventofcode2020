def find_loop(infile):
	with open(infile, 'r') as f:
		instruction_list = []
		for row in f:
			inst = row.strip().split()
			instruction_list.append((inst[0], int(inst[1])))
	next_inst = 0
	acc = 0
	seen = set()
	while next_inst not in seen:
		seen.add(next_inst)
		inst, shift = instruction_list[next_inst]
		if inst == 'nop':
			next_inst += 1
		elif inst == 'acc':
			acc += shift
			next_inst += 1
		elif inst == 'jmp':
			next_inst += shift
	return acc

if __name__ == '__main__':
	infile = 'Advent8.txt'
	print(find_loop(infile))