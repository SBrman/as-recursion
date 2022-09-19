import time

class Image:
    def __init__(self, data):
        self.data = data
        self.height = len(data)
        self.width = len(data[0])
    
    def __str__(self):
        return "\n".join([''.join(row) for row in self.data]) + '\n\n'

    def __getitem__(self, ij):
        i, j = ij
        return self.data[i][j]

    def __setitem__(self, ij, value):
        i, j = ij
        self.data[i][j] = value


def flood_fill_iterative(image, x, y, newChar, oldChar=None):
    if oldChar is None:
        oldChar = image[y, x]

    stack = []
    stack.append((x, y))

    while stack:
        x, y = stack.pop()

        if oldChar == newChar or image[y, x] != oldChar:
            continue 

        image[y, x] = newChar
        print(image)
        time.sleep(.1)

        if y + 1 < image.height: stack.append((x, y+1))
        if y - 1 >= 0: stack.append((x, y-1))
        if x + 1 < image.width: stack.append((x+1, y))
        if x - 1 >= 0: stack.append((x-1, y))


if __name__ == "__main__":
    data = [
              list('.....................................'),
              list('..########################...........'),
              list('..#......................#...#####...'),
              list('..#..........########....#####...#...'),
              list('..#..........#......#............#...'),
              list('..#..........########.........####...'),
              list('..######......................#......'),
              list('.......#..#####.....###########......'),
              list('.......####...#######................'),
              list('.....................................')
           ]

    image = Image(data)
    print(image)
    flood_fill_iterative(image, 3, 3, 'o')
