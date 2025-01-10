import sys
input = sys.stdin.readline

def main():
    n = int(input())
    is_zero = False
    plus = []
    one = 0
    minus = []
    for _ in range(n):
        x = int(input())
        if x == 0:
            is_zero = True
        elif x == 1:
            one += 1
        elif x > 0:
            plus.append(x)
        else:
            minus.append(x)
    plus.sort(reverse=True)
    minus.sort()
    answer = 0
    for a, b in zip(plus[0::2], plus[1::2]):
        answer += a * b
    if len(plus) % 2:
        answer += plus[-1]
    for a, b in zip(minus[0::2], minus[1::2]):
        answer += a * b
    if len(minus) % 2 and not is_zero:
        answer += minus[-1]
    answer += one
    print(answer)

if __name__ == "__main__":
    main()