def ppt_batch_validate(infile):
	#154 is too high
	#124 is too low
	with open(infile, 'r') as f:
		passport = {}
		valid_ppts = 0
		fields_check = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

		for row in f:
			data = row.strip()
			if data == '':
				if fields_check.difference(set(passport.keys())) != set():
					missing_field = True
				else:
					if all(field_valid(field, entry) for field,entry in passport.items()):
						valid_ppts += 1
				passport = {}
			else:
				for cell in data.split():
					field, entry = cell.split(':')
					passport[field] = entry
		if fields_check.difference(set(passport.keys())) != set():
			return valid_ppts
		else:
			if all(field_valid(field, entry) for field,entry in passport.items()):
				valid_ppts += 1
	return valid_ppts

def field_valid(field, entry):
	if field == 'byr':
		if len(entry) == 4 and entry.isnumeric() and 1920 <= int(entry) <= 2002:
			byr = True
		else:
			return False
	elif field == 'iyr':
		if len(entry) == 4 and entry.isnumeric() and 2010 <= int(entry) <= 2020:
			iyr = True
		else:
			return False
	elif field == 'eyr':
		if len(entry) == 4 and entry.isnumeric() and 2020 <= int(entry) <= 2030:
			eyr = True
		else:
			return False
	elif field == 'hgt':
		try:
			ms, un = entry[:-2], entry[-2:]
		except:
			return False
		if un == 'in' and ms.isnumeric() and 59 <= int(ms) <= 76:
			hgt = True
		elif un == 'cm' and ms.isnumeric() and 150 <= int(ms) <= 193:
			hgt = True
		else:
			return False
	elif field == 'hcl':
		if entry[0] == '#' and len(entry) == 7:
			if not all(c in '0123456789abcdef' for c in entry[1:]):
				return False
	elif field == 'ecl':
		if entry not in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}:
			return False
	elif field == 'pid':
		if not (len(entry) == 9 and entry.isnumeric()):
			return False
	elif field != 'cid':
		return False
	return True

if __name__ == '__main__':
	infile = 'Advent4.txt'
	print(ppt_batch_validate(infile))