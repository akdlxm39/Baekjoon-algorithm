import sys
input = sys.stdin.readline

def main():
    for _ in range(int(input())):
        str = input().rstrip()
        l, r = 0, len(str)-1
        while l < r and str[l] == str[r]:
            l += 1
            r -= 1
        if l >= r:
            print(0)
            continue
        l1, r1 = l+1, r
        while l1 < r1 and str[l1] == str[r1]:
            l1 += 1
            r1 -= 1
        if l1 >= r1:
            print(1)
            continue
        l2, r2 = l, r-1
        while l2 < r2 and str[l2] == str[r2]:
            l2 += 1
            r2 -= 1
        if l2 >= r2:
            print(1)
        else:
            print(2)

if __name__ == "__main__":
    main()