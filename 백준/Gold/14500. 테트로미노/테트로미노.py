import sys
input = sys.stdin.readline

tetromino_shape = {(0,3):[((0,0),(0,1),(0,2),(0,3))],
                   (3,0):[((0,0),(1,0),(2,0),(3,0))],
                   (1,1):[((0,0),(1,0),(0,1),(1,1))],
                   (1,2):[((0,0),(1,0),(1,1),(1,2)),
                          ((0,1),(1,0),(1,1),(1,2)),
                          ((0,2),(1,0),(1,1),(1,2)),
                          ((0,0),(0,1),(0,2),(1,0)),
                          ((0,0),(0,1),(0,2),(1,1)),
                          ((0,0),(0,1),(0,2),(1,2)),
                          ((0,0),(0,1),(1,1),(1,2)),
                          ((0,1),(0,2),(1,0),(1,1))],
                   (2,1):[((0,0),(1,0),(2,0),(0,1)),
                          ((0,0),(1,0),(2,0),(1,1)),
                          ((0,0),(1,0),(2,0),(2,1)),
                          ((0,0),(0,1),(1,1),(2,1)),
                          ((1,0),(0,1),(1,1),(2,1)),
                          ((2,0),(0,1),(1,1),(2,1)),
                          ((0,0),(1,0),(1,1),(2,1)),
                          ((1,0),(2,0),(0,1),(1,1))]}

def main():
    n, m = map(int, input().split())
    paper = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for key in tetromino_shape.keys():
        for i in range(n-key[0]):
            for j in range(m-key[1]):
                for shape in tetromino_shape[key]:
                    shape_sum = 0
                    for dx, dy in shape:
                        shape_sum += paper[i+dx][j+dy]
                    ans = max(ans, shape_sum)
    print(ans)

if __name__ == "__main__":
    main()