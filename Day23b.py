from collections import deque

class cupsGame:
    def __init__(self, cups_list, max_cup):
        self.cups_list = deque(cups_list+list(range(10,max_cup+1)))
        self.max = max_cup

    def make_move(self):
        this_cup = self.cups_list.popleft()
        dest = this_cup - 1
        picked_up = [self.cups_list.popleft() for _ in range(3)]
        if dest == 0:
            dest = self.max
        while dest in picked_up:
            dest -= 1
            if dest == 0:
                dest = self.max
        #cProfile says I'm spending all my time here, which makes sense
        drop = self.cups_list.index(dest)+1
        for _ in range(3):
            self.cups_list.insert(drop, picked_up.pop())
        self.cups_list.append(this_cup)


    def play_game(self, rounds):
        pos = 0
        while rounds:
            rounds -= 1
            self.make_move()
        idx = self.cups_list.index(1)
        return [self.cups_list[idx+1],self.cups_list[idx+2]]

if __name__ == '__main__':
    game = cupsGame([7,1,6,8,9,2,5,4,3], 10**6)
    # print(play_game(cups_list, 100))