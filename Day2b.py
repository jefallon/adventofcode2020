def c4(infile):
    valid = 0
    with open(infile ,'r') as f:
        for row in f:
            rng, let, pw = row.strip().split(' ')
            lo, hi = map(int, rng.split('-'))
            let = let[0]
            if (pw[lo-1]+pw[hi-1]).count(let) == 1:
                valid += 1
    return valid

if __name__ == '__main__':
    infile ='Advent2.txt'
    print(c4(infile))