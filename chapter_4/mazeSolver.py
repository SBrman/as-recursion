import time


class OutOfBoundaryError(Exception):
    pass


class Maze:
    def __init__(self, data):

        self.__original_data = [list(line[8:]) for line in data.split('\n')[1:-1]]
        self.temp_data_stack = [self.__original_data.copy()]
        self.data = self.__original_data.copy()

        self.width = max(len(list(line)) for line in self.data)
        self.height = len(data)

        self.start = self.find('S')
        self.new_character = '.'
        self.visited = set()
        
    def __str__(self):
        return "\n" + "\n".join(['  ' + ''.join(line) for line in self.data]) + "\n"

    def __setitem__(self, key, value):
        y, x = key
        value = str(value)
        assert len(value) == 1, "Can't put more than one character."
        if not self.can_move(y, x):
            raise OutOfBoundaryError("Out of boundary.")
        self.data[y][x] = value

    def __getitem__(self, key):
        y, x = key
        return self.data[y][x]
    
    def can_move(self, y, x):
        return 0 <= y < self.height and 0 <= x < self.width and self.data[y][x] != "#"

    def find(self, character):
        for y, row in enumerate(self.data):
            for x, value in enumerate(row):
                if value == character:
                    return (y, x)

    def get_new_xy(self, y, x, direction):
        if direction == 'up':
            y += 1
        elif direction == 'down':
            y -= 1
        elif direction == 'left':
            x -= 1
        elif direction == 'right':
            x += 1
        else:
            raise Exception("Unknown direction.")
        return y, x

    def move(self, y, x):
        self[y, x] = self.new_character
        print(self)
        time.sleep(0.01)
    
    def unmove(self, y, x):
        self[y, x] = ' '
        print(self)
        time.sleep(0.01)

    def solve(self, y, x):
        if self[y, x] == 'E':
            return True
        if (y, x) in self.visited:
            return False

        self.visited.add((y, x))

        if self.can_move(y, x):
            self.move(y, x)
        else:
            return False
        
        for direction in {'up', 'down', 'left', 'right'}:    
            new_y, new_x = self.get_new_xy(y, x, direction)
            solved = self.solve(new_y, new_x)
            if solved:
                return True

        self.unmove(y, x)
        return False


if __name__ == "__main__":


    data = """
        #######################################################################
        #S#                 #       # #   #     #         #     #   #         #
        # ##### ######### # ### ### # # # # ### # # ##### # ### # # ##### # ###
        # #   #     #     #     #   # # #   # #   # #       # # # #     # #   #
        # # # ##### # ########### ### # ##### ##### ######### # # ##### ### # #
        #   #     # # #     #   #   #   #         #       #   #   #   #   # # #
        ######### # # # ##### # ### # ########### ####### # # ##### ##### ### #
        #       # # # #     # #     # #   #   #   #     # # #   #         #   #
        # # ##### # # ### # # ####### # # # # # # # ##### ### ### ######### # #
        # # #   # # #   # # #     #     #   #   #   #   #   #     #         # #
        ### # # # # ### # # ##### ####### ########### # ### # ##### ##### ### #
        #   # #   # #   # #     #   #     #       #   #     # #     #     #   #
        # ### ####### ##### ### ### ####### ##### # ######### ### ### ##### ###
        #   #         #     #     #       #   # #   # #     #   # #   # #   # #
        ### ########### # ####### ####### ### # ##### # # ##### # # ### # ### #
        #   #   #       # #     #   #   #     #       # # #     # # #   # #   #
        # ### # # ####### # ### ##### # ####### ### ### # # ####### # # # ### #
        #     #         #     #       #           #     #           # #      E#
        #######################################################################
        """
    m = Maze(data)

    print(m)
    m.solve(*m.start)

