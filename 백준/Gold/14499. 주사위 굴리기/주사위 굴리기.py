import sys
input = sys.stdin.readline
dx = (0, 0, 0, -1, 1)
dy = (0, 1, -1, 0, 0)

class Dice:
    rotation = {1:["top", "right", "bottom", "left"],
                2:["top", "left", "bottom", "right"],
                3:["top", "up", "bottom", "down"],
                4:["top", "down", "bottom", "up"]}

    def __init__(self):
        self.nums = {"top":0, "bottom":0, "left":0, "right":0, "up":0, "down":0}

    def move(self, direction):
        tmp = 0
        for s in Dice.rotation[direction]:
            tmp, self.nums[s] = self.nums[s], tmp
        self.nums["top"] = tmp

def main():
    n, m, x, y, k = map(int, input().split())
    map_ = [list(map(int, input().split())) for _ in range(n)]
    dice = Dice()
    for direction in map(int, input().split()):
        nx, ny = x+dx[direction], y+dy[direction]
        if not (0<=nx<n and 0<=ny<m):
            continue
        x, y = nx, ny
        dice.move(direction)
        if map_[x][y]:
            dice.nums["bottom"] = map_[x][y]
            map_[x][y] = 0
        else:
            map_[x][y] = dice.nums["bottom"]
        print(dice.nums["top"])

if __name__ == "__main__":
    main()