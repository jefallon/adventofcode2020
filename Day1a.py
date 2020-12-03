def seek_pair(infile):
    expense_report = set()
    with open(infile, 'r') as f:
        for row in f:
            expense = int(row)
            pair = 2020 - expense
            if pair in expense_report:
                return expense*pair
            expense_report.add(expense)

if __name__ == '__main__':
    infile = 'Advent1.txt'
    print(seek_pair(infile))