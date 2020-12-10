def make_adapters(infile):
	adapters = [0]
	with open(infile, 'r') as f:
		for row in f:
			adapters.append(int(row.strip()))
		adapters.append
	adapters.sort(reverse = True)
	adapters = [adapters[0] + 3] + adapters
	return adapters

def count_paths(adapters):
	paths = {}
	paths[adapters[0]] = 1
	for i, a in enumerate(adapters[:-3]):
		for adapter in adapters[i+1: i+4]:
			if a - adapter <= 3:
				paths[adapter] = paths.get(adapter, 0) + paths[a]
	for i in range(-3,-1):
		for adapter in adapters[i+1:]:
			paths[adapter] = paths.get(adapter, 0) + paths[adapters[i]]
	return paths[0]

if __name__ == '__main__':
	infile = 'Advent10.txt'
	adapters = make_adapters(infile)
	print(count_paths(adapters))