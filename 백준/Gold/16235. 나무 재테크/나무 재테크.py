import sys
input = sys.stdin.readline
di = [-1, -1, -1, 0, 0, 1, 1, 1]
dj = [-1, 0, 1, -1, 1, -1, 0, 1]

def main():
    n, m, k = map(int, input().split())
    soils = [[5]*n for _ in range(n)]
    nutrients = [list(map(int, input().split())) for _ in range(n)]
    trees = [[{} for _ in range(n)] for _ in range(n)]
    temp_trees = [[0]*n for _ in range(n)]
    for _ in range(m):
        x, y, z = map(int, input().split())
        trees[x-1][y-1][z] = 1
    for _ in range(k):
        for i in range(n):
            for j in range(n):
                temp_nutrient = 0
                temp_tree = {}
                for age in sorted(trees[i][j].keys()):
                    cnt = trees[i][j][age]
                    alive = min(cnt, soils[i][j]//age)
                    if alive:
                        soils[i][j] -= alive * age
                        temp_tree[age+1] = alive
                        if (age+1) % 5 == 0:
                            temp_trees[i][j] += alive
                    dead = cnt - alive
                    if dead:
                        temp_nutrient += (age//2) * dead
                trees[i][j] = temp_tree
                soils[i][j] += temp_nutrient
        for i in range(n):
            for j in range(n):
                if temp_trees[i][j]:
                    for d in range(8):
                        ni, nj = i+di[d], j+dj[d]
                        if 0<=ni<n and 0<=nj<n:
                            trees[ni][nj][1] = trees[ni][nj].get(1, 0) + temp_trees[i][j]
                    temp_trees[i][j] = 0
                soils[i][j] += nutrients[i][j]
    print(sum(sum(trees[i][j].values()) for i in range(n) for j in range(n)))

if __name__ == "__main__":
    main()