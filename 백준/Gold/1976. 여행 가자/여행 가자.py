import sys
input = sys.stdin.readline

def main():
    n, m = int(input()), int(input())
    roads = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        roads[i][i] = 1
    course = list(map(lambda x:int(x)-1, input().split()))
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if roads[i][k] and roads[k][j]:
                    roads[i][j] = 1
    for i in range(m-1):
        s, e = course[i], course[i+1]
        if not roads[s][e]:
            print("NO")
            break
    else:
        print("YES")

if __name__ == "__main__":
    main()