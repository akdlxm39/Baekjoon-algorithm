import sys
input = sys.stdin.readline

def main():
    n = int(input())
    s = set()
    for _ in range(n):
        command = input().split()
        if command[0] == 'add':
            s.add(int(command[1]))
        elif command[0] == 'remove':
            s.discard(int(command[1]))
        elif command[0] == 'check':
            print(int(int(command[1]) in s))
        elif command[0] == 'toggle':
            s ^= {int(command[1])}
        elif command[0] == 'all':
            s |= set(range(1, 21))
        elif command[0] == 'empty':
            s.clear()


if __name__ == "__main__":
    main()