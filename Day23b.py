def cups_game(cycle, rounds):
    cur_val = cycle[0]
    max_val = 10**6

    cycle_dict = dict(zip(cycle, cycle[1:]))
    cycle_dict[cycle[-1]] = cur_val

    def pick_up():
        pick = [cycle_dict[cur_val]]
        for _ in range(2):
            pick.append(cycle_dict[pick[-1]])
        return pick

    while rounds:
        rounds -= 1
        pick = pick_up()

        next_val = cur_val-1
        while next_val <= 0 or next_val in pick:
            next_val -= 1
            if next_val <= 0:
                next_val = max_val

        cycle_dict[cur_val] = cycle_dict[pick[-1]]
        cycle_dict[pick[-1]] = cycle_dict[next_val]
        cycle_dict[next_val] = pick[0]


        cur_val = cycle_dict[cur_val]

    return cycle_dict

def seed_game(cups_list, max):
    long_cycle = cups_list + list(range(10, max+1))
    return long_cycle

if __name__ == '__main__':
    game_state = seed_game([7,1,6,8,9,2,5,4,3], 10**6)
    end_state = cups_game(game_state, 10**7)
    star_1 = end_state[1]
    star_2 = end_state[star_1]
    print(star_1*star_2)