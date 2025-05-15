import sys
input = sys.stdin.readline
modular = 1234567891

def main():
    l, string = int(input()), input().rstrip()
    ans = 0
    for i in range(l):
        ans += (ord(string[i])-96)*(31**i)%modular
    print(ans%modular)

if __name__ == "__main__":
    main()