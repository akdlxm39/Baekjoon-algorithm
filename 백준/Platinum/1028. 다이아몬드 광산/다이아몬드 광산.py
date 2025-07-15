import sys
input = sys.stdin.readline

def main():
    r, c = map(int, input().split())
    mines = [input().rstrip() for _ in range(r)]
    left = [[-1] * (c + 1) for _ in range(r + 1)]
    right = [[-1] * (c + 1) for _ in range(r + 1)]
    for i in range(r - 1, -1, -1):
        for j in range(c):
            if mines[i][j] == '0': continue
            left[i][j] = left[i + 1][j - 1] + 1
            right[i][j] = right[i + 1][j + 1] + 1
    max_size = -1
    for i in range(r):
        for j in range(c):
            size = min(left[i][j], right[i][j])
            for tmp_size in range(size, max_size, -1):
                if not (i + tmp_size < r and 0 <= j - tmp_size and j + tmp_size < c): continue
                if tmp_size <= right[i + tmp_size][j - tmp_size] and tmp_size <= left[i + tmp_size][j + tmp_size]:
                    max_size = tmp_size
                    break
    print(max_size + 1)


if __name__ == "__main__":
    main()