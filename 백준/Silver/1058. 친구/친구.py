import sys
input = sys.stdin.readline

def main():
    n = int(input())
    friends = [list(input().rstrip()) for _ in range(n)]
    friends2 = [0]*n
    for i in range(n):
        tmp = friends[i][:]
        for j in range(n):
            if friends[i][j] == 'Y':
                for k in range(n):
                    if friends[j][k] == 'Y':
                        tmp[k] = 'Y'
        friends2[i] = tmp.count('Y') - (tmp[i]=='Y')
    print(max(friends2))

if __name__ == "__main__":
    main()