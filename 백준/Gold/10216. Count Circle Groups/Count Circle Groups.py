import sys, os, io
from math import sqrt
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

def main():
    for _ in range(int(input())):
        n = int(input())
        circle_group = {0:[tuple(map(int, input().split()))]}
        for i in range(1, n):
            x1, y1, r1 = map(int, input().split())
            flag = -1
            for j, circles in tuple(circle_group.items()):
                if flag == -1:
                    for x2, y2, r2 in circles:
                        if r1 + r2 >= sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)):
                            circle_group[j].append((x1, y1, r1))
                            flag = j
                            break
                else:
                    for x2, y2, r2 in circles:
                        if r1 + r2 >= sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)):
                            circle_group[flag] += circle_group[j]
                            del circle_group[j]
                            break
            if flag == -1:
                circle_group[i] = [(x1, y1, r1)]
        print(len(circle_group))

if __name__ == "__main__":
    main()