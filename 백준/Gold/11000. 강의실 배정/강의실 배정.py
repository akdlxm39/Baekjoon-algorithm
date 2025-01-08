import sys
from heapq import heapify, heappush, heappop, heappushpop
input = sys.stdin.readline

def main():
    n = int(input())
    course = sorted([tuple(map(int, input().split())) for _ in range(n)])    
    classroom = [0]
    for s, e in course:
        if classroom[0] <= s:
            heappushpop(classroom, e)
        else:
            heappush(classroom, e)
    print(len(classroom))

if __name__ == "__main__":
    main()