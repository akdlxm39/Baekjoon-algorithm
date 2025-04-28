import sys
input = sys.stdin.readline

def main():
    A, B, C = map(int, input().split())
    answer = devide(A, B, C)
    print(answer)

def devide(A, B, C):
    if B == 1:
        return A % C
    tmp1 = devide(A, B//2, C)
    tmp2 = (tmp1 ** 2) % C
    return (tmp2 * A) % C if B % 2 else tmp2

main()