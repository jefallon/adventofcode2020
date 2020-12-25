def make_move(cups_list):
    picked_up = [cups_list.pop(1) for _ in range(3)]
    this_cup = cups_list[0]
    if min(cups_list) == this_cup:
        dest = max(cups_list)
    else:
        dest = max(cup for cup in cups_list if cup < this_cup)
    dest_idx = cups_list.index(dest)
    cups_list = cups_list[1:dest_idx+1]+picked_up+cups_list[dest_idx+1:]+[this_cup]
    return cups_list

def play_game(cups_list, rounds):
    while rounds:
        rounds -= 1
        cups_list = make_move(cups_list)
    idx = cups_list.index('1')
    cups_list = cups_list[idx+1:]+cups_list[:idx]
    return ''.join(cups_list)

if __name__ == '__main__':
    print(play_game(list('716892543'), 100))