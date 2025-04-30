import sys
input = sys.stdin.readline

def main():
    n = int(input())
    queue = []
    head = 0
    tail = 0
    for _ in range(n):
        command = input().split()
        if command[0] == 'push':
            queue.append(int(command[1]))
            tail += 1
        elif command[0] == 'pop':
            if head < tail:
                print(queue[head])
                head += 1
            else:
                print(-1)
        elif command[0] == 'size':
            print(tail - head)
        elif command[0] == 'empty':
            print(int(head==tail))
        elif command[0] == 'front':
            print(queue[head] if head < tail else -1)
        elif command[0] == 'back':
            print(queue[tail-1] if head < tail else -1)

if __name__ == "__main__":
    main()