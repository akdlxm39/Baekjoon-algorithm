import sys
input = sys.stdin.readline

def solve(x, m, size):
    if size == 0:
        return True
    for i in range(size):
        if x[m-i-1] == x[m+i+1]:
            return False
    if solve(x, m-size//2-1, size//2) and solve(x, m+size//2+1, size//2):
        return True
    return False

def main():
    for _ in range(int(input())):
        x = list(map(int, list(input().rstrip())))
        if solve(x, len(x)//2, len(x)//2):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()