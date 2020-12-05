def ppt_batch_check(infile):
	with open(infile, 'r') as f:
		ppt_fields = set()
		valid_ppts = 0
		fields_check = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
		for row in f:
			data = row.strip()
			if data == "":
				if fields_check.difference(ppt_fields) == set():
					valid_ppts += 1
				ppt_fields = set()
			else:
				for field in data.split():
					ppt_fields.add(field.split(':')[0])
		if fields_check.difference(ppt_fields) == set():
			valid_ppts += 1
		ppt_fields = set()		
		return valid_ppts

if __name__ == '__main__':
	infile = 'Advent4.txt'
	print(ppt_batch_check(infile))