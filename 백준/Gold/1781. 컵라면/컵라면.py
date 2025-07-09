import sys
from heapq import heappush, heappop, heapify
input = sys.stdin.readline

def main():
    n = int(input())
    problems = {}
    for _ in range(n):
        deadline, reward = map(int, input().split())
        problems.setdefault(deadline, []).append(reward)
    deadlines = sorted(problems.keys(), reverse=True)
    heap = []
    ans = idx = 0
    for i in range(n, 0, -1):
        while idx < len(deadlines) and deadlines[idx] >= i:
            for reward in problems[deadlines[idx]]:
                heappush(heap, -reward)
            idx += 1
        if heap:
            ans -= heappop(heap)
    print(ans)

if __name__ == "__main__":
    main()