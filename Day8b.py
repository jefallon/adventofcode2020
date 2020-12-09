def set_instructions(infile):
	with open(infile, 'r') as f:
		instruction_list = []
		for row in f:
			inst = row.strip().split()
			instruction_list.append([inst[0], int(inst[1])])
	return instruction_list

def find_loop(instruction_list):
	next_inst = 0
	acc = 0
	seen = set()
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
		return False

def find_exit_acc(instruction_list):
	for i, test_val in enumerate(instruction_list):
		if test_val[0] in {'nop','jmp'} and test_val[1] != 0:
			new_list = instruction_list[:i]+[[swap(test_val[0]), test_val[1]]]+instruction_list[i+1:]
			acc = find_loop(new_list)
			if acc:
				return acc

def swap(test_val):
	if test_val == 'nop':
		return 'jmp'
	elif test_val == 'jmp':
		return 'nop'



if __name__ == '__main__':
	infile = 'Advent8.txt'
	instruction_list = set_instructions(infile)
	print(find_exit_acc(instruction_list))