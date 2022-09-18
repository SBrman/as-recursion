import time


class Disk:
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        text = '@' * self.value + f"_{self.value}_" + '@' * self.value
        return str(text.center(CENTER, ' ')) + '\n'

    def __lt__(self, other):
        return self.value < other.value


class Tower:
    def __init__(self, name):
        self.name = name
        self._disks = []

    def __str__(self):

        pipes_number =  TOTAL_DISKS + 3 - len(self._disks)
        pipes = "| |".center(CENTER, ' ') + '\n'

        text = pipes * pipes_number

        for disk in self._disks[::-1]:
            text += str(disk)

        text += '-' * CENTER + '\n'
        text += ' ' + f" {self.name} ".center(28, ' ') + ' \n'
        text += '-' * CENTER + '\n'

        return text
    
    @property
    def disks(self):
        return self._disks
            
    def push(self, disk):
        assert self._disks == [] or self._disks[-1] > disk, f"Disk {disk.value} is higher than {self._disks[-1].value}"
        self._disks.append(disk)
    
    def pop(self):
        return self._disks.pop()


class TowerOfHanoi:
    def __init__(self, towers):
        self.towers = towers
        self.solved = False
    
    def __str__(self):
        text = ""
        tower_texts = [str(tower).split('\n') for tower in self.towers]
        for i in range(len(tower_texts[0])):
            for j in range(len(tower_texts)):
                text += tower_texts[j][i] + '  '
            text += '\n'    
        return text

    def solve(self):
        a, b, c = self.towers
        self.move_disks(a, c, b)
            
    def move_a_disk(self, start: Tower, end: Tower):        
        disk = start.pop()
        end.push(disk)
        print(self)
        time.sleep(0.5)
    
    def move_disks(self, start: Tower, end: Tower, via: Tower, number_of_disks: int = None):
        if number_of_disks is None:
            number_of_disks = len(self.towers[0].disks)
        if number_of_disks == 1:
            self.move_a_disk(start, end)
            print(self)
            return
        else:
            self.move_disks(start, via, end, number_of_disks-1)
            self.move_a_disk(start, end)
            self.move_disks(via, end, start, number_of_disks-1)
            return

if __name__ == "__main__":
    
    TOTAL_DISKS = 6
    # assert TOTAL_DISKS < 10, "Total disks more than 10 not allowed. (Can't pretty print.)"
    CENTER = TOTAL_DISKS * 5


    A = Tower("A")
    for i in list(range(TOTAL_DISKS, 0, -1)):
        disk = Disk(i)
        A.push(disk) 

    B = Tower("B")
    C = Tower("C")

    Game = TowerOfHanoi([A, B, C])
    print(Game)

    Game.solve()

