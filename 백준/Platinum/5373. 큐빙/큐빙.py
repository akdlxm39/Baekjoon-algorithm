import sys
input = sys.stdin.readline

class Cube:
    rotation_dict = {'U':(('B', 0, 2, 1), ('R', 0, 0, -1), ('F', 0, 0, -1), ('L', 0, 0, -1), ('B', 0, 2, 1)),
                     'D':(('F', 0, 2, 1), ('R', 0, 2, 1), ('B', 0, 0, -1), ('L', 0, 2, 1), ('F', 0, 2, 1)),
                     'F':(('U', 0, 2, 1), ('R', 1, 0, 1), ('D', 0, 0, -1), ('L', 1, 2, -1), ('U', 0, 2, 1)),
                     'B':(('D', 0, 2, 1), ('R', 1, 2, -1), ('U', 0, 0, -1), ('L', 1, 0, 1), ('D', 0, 2, 1)),
                     'L':(('U', 1, 0, 1), ('F', 1, 0, 1), ('D', 1, 0, 1), ('B', 1, 0, 1), ('U', 1, 0, 1)),
                     'R':(('U', 1, 2, -1), ('B', 1, 2, -1), ('D', 1, 2, -1), ('F', 1, 2, -1), ('U', 1, 2, -1)),
                     '+':((0,0), (0,2), (2,2), (2,0), (0,0), (0,1), (1,2), (2,1), (1,0), (0,1)),
                     '-':((0,0), (2,0), (2,2), (0,2), (0,0), (1,0), (2,1), (1,2), (0,1), (1,0))}

    def __init__(self):
        self.side = {'U':[['w']*3 for _ in range(3)],
                     'D':[['y']*3 for _ in range(3)],
                     'F':[['r']*3 for _ in range(3)],
                     'B':[['o']*3 for _ in range(3)],
                     'L':[['g']*3 for _ in range(3)],
                     'R':[['b']*3 for _ in range(3)]}

    def rotation(self, command):
        key = command[0]
        dir = 1 if command[1] == '+' else -1
        cur = self.side[key]
        tmp = '1'
        for x,y in Cube.rotation_dict[command[1]]:
            tmp, cur[x][y] = cur[x][y], tmp
        tmp = ['1', '2', '3']
        for side_key, rowcol, idx, side_dir in Cube.rotation_dict[key][::dir]:
            if rowcol == 0:
                self.side[side_key][idx][::side_dir], tmp = tmp, self.side[side_key][idx][::side_dir]
            else:
                if side_dir == 1:
                    for i in range(3):
                        tmp[i], self.side[side_key][i][idx] = self.side[side_key][i][idx], tmp[i]
                else:
                    for i in range(3):
                        tmp[i], self.side[side_key][2-i][idx] = self.side[side_key][2-i][idx], tmp[i]

def main():
    for _ in range(int(input())):
        n = int(input())
        cube = Cube()
        for command in input().split():
            cube.rotation(command)
        print('\n'.join(map(''.join, cube.side['U'])))

if __name__ == "__main__":
    main()