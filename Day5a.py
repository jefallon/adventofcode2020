code_dict = {'B': '1', 'F': '0', 'R': '1', 'L':'0'}

def seat_val(seat_code):
    row = ''.join([code_dict[d] for d in seat_code[:7]])
    seat = ''.join([code_dict[d] for d in seat_code[7:]])
    row = int(row, base = 2)
    seat = int(seat, base = 2)
    seat_ID = row * 8 + seat
    return seat_ID

def max_seat_ID(infile):
    max_ID = 0
    with open(infile, 'r') as f:
        for boarding_pass in f:
            max_ID = max(max_ID, seat_val(boarding_pass.strip()))
    return max_ID

if __name__ == '__main__':
    infile = 'Advent5.txt'
    print(max_seat_ID(infile))