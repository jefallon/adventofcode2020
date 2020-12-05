code_dict = {'B': '1', 'F': '0', 'R': '1', 'L':'0'}

def seat_val(seat_code):
    row = ''.join([code_dict[d] for d in seat_code[:7]])
    seat = ''.join([code_dict[d] for d in seat_code[7:]])
    row = int(row, base = 2)
    seat = int(seat, base = 2)
    seat_ID = row * 8 + seat
    return seat_ID

def all_seat_IDs(infile):
    boarding_passes = set()
    with open(infile, 'r') as f:
        for boarding_pass in f:
            boarding_passes.add(seat_val(boarding_pass.strip()))
    return boarding_passes

def find_my_seat():
    boarding_passes = all_seat_IDs(infile)
    last_seat = max(boarding_passes)
    first_seat = min(boarding_passes)
    return set(range(first_seat, last_seat)).difference(boarding_passes)

if __name__ == '__main__':
    infile = 'Advent5.txt'
    print(find_my_seat())