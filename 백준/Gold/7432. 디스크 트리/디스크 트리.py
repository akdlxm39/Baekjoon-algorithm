import sys
input = sys.stdin.readline

def main():
    n = int(input())
    dirs = sorted(input().rstrip().split('\\') for _ in range(n))
    ans = [' '*blank + dir for blank, dir in enumerate(dirs[0])]
    for i in range(1, len(dirs)):
        cnt = 0
        while cnt <len(dirs[i-1]) and cnt < len(dirs[i]) and dirs[i-1][cnt] == dirs[i][cnt]:
            cnt += 1
        for blank, dir in enumerate(dirs[i][cnt:], cnt):
            ans.append(' '*blank + dir)
    print('\n'.join(ans))

if __name__ == "__main__":
    main()