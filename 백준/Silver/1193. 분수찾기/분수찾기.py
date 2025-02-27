import sys
input = sys.stdin.readline
X = int(input())
i = 1
while X > i:
    X -= i
    i += 1
print(f"{X}/{i+1-X}" if i % 2 == 0 else f"{i+1-X}/{X}")
