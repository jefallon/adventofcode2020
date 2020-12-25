import re

class Solution():

    def __init__(self):
        self.nbr = re.compile('se|sw|ne|nw|e|w')
        self.tiles = {}
        self.min_row = 0
        self.min_col = 0
        self.max_row = 0
        self.max_col = 0

    def get_neighbors(self, row, col):
        nbrs = [self.take_step(step, row, col) for step in ['e', 'w', 'nw', 'se', 'sw', 'ne']]
        return nbrs

    def take_step(self, step, row, col):
        if step == 'e':
            col += 1
        elif step == 'w':
            col -= 1
        elif step == 'nw':
            row += 1
        elif step == 'se':
            row -= 1
        elif step == 'ne':
            row += 1
            col += 1
        elif step == 'sw':
            row -= 1
            col -= 1
        return row, col

    def follow_inst(self, inst):
        row = 0
        col = 0
        for step in re.findall(self.nbr, inst):
            row, col = self.take_step(step, row, col)
        if row > self.max_row:
            self.max_row = row
        elif row < self.min_row:
            self.min_row = row
        if col > self.max_col:
            self.max_col = col
        elif col < self.min_col:
            self.min_col = col
        return row, col

    def flip_tile(self, row, col):
        self.tiles[(row, col)] = self.tiles.get((row, col), 0) ^ 1

    def day_pass(self):
        to_flip = {}
        self.min_row -=1
        self.max_row += 1
        self.min_col -= 1
        self.max_col += 1
        for row in range(self.min_row, self.max_row+1):
            for col in range(self.min_col, self.max_col+1):
                nbrs = self.get_neighbors(row, col)
                blk_nbrs = sum(self.tiles.get(nbr, 0) for nbr in nbrs)
                this_tile =self.tiles.get((row, col), 0)
                if this_tile == 1 and blk_nbrs not in {1,2}:
                    to_flip[(row, col)] = 0
                elif this_tile == 0 and blk_nbrs == 2:
                    to_flip[(row, col)] = 1
        self.tiles.update(to_flip)



if __name__ == '__main__':
    infile = 'Advent24.txt'
    s = Solution()
    with open(infile, 'r') as f:
        for row in f:
            tile = s.follow_inst(row.strip())
            s.flip_tile(tile[0], tile[1])
    for day in range(100):
        s.day_pass()
    print(sum(s.tiles.values()))