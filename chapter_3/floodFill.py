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


def flood_fill(image, x, y, newChar, oldChar=None):
    if oldChar is None:
        oldChar = image[y, x]
    if oldChar == newChar or image[y, x] != oldChar:
        return
    image[y, x] = newChar
    print(image)
    time.sleep(.1)
    if y + 1 < image.height:
        flood_fill(image, x, y+1, newChar, oldChar)
    if y - 1 >= 0:
        flood_fill(image, x, y-1, newChar, oldChar)
    if x + 1 < image.width:
        flood_fill(image, x+1, y, newChar, oldChar)
    if x - 1 >= 0:
        flood_fill(image, x-1, y, newChar, oldChar)
    return


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
    flood_fill(image, 3, 3, 'o')
