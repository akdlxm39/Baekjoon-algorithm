import sys
input = sys.stdin.readline
a, b, c, d, e, f = map(int, input().split())
if b == 0:
    x = c // a
    y = (f - d*x) // e
elif e == 0:
    x = f // d
    y = (c - a * x) // b
else:
    x = (c*e - b*f) // (a*e - b*d)
    y = (c - a * x) // b
print(x, y)