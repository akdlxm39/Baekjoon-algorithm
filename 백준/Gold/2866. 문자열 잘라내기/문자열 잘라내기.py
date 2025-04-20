import sys
input = sys.stdin.readline

def main():
    r, c = map(int, input().split())
    strings = [input().rstrip() for _ in range(r)]
    cstrings = list(strings[-1])
    idx = r-1
    while idx > 0 and len(set(cstrings)) != c:
        idx -= 1
        for i, char in enumerate(strings[idx]):
            cstrings[i] += char
    print(idx)

if __name__ == "__main__":
    main()