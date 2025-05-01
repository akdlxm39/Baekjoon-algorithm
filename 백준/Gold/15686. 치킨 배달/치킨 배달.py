import sys
from heapq import heapify, heappop
input = sys.stdin.readline

def get_chicken_distance(n, city):
    chickens = []
    houses = []
    chicken_distance = {}
    for i in range(n):
        for j in range(n):
            if city[i][j] == 1:
                houses.append((i, j))
            elif city[i][j] == 2:
                chickens.append((i, j))
    for chicken in chickens:
        chicken_distance[chicken] = []
        for hx, hy in houses:
            dist = abs(chicken[0] - hx) + abs(chicken[1] - hy)
            chicken_distance[chicken].append((dist, hx, hy))
    return chickens, chicken_distance, len(houses)

def bruteforce(n, m, city, chickens, chicken_distance, house_cnt, chosen, chicken_idx, ans):
    if len(chosen) == m:
        dist = check_distance(chickens, chosen, chicken_distance, house_cnt)
        ans[0] = min(ans[0], dist)
        return
    bruteforce(n, m, city, chickens, chicken_distance, house_cnt, chosen+[chicken_idx], chicken_idx+1, ans)
    if len(chickens) - chicken_idx > m - len(chosen):
        bruteforce(n, m, city, chickens, chicken_distance, house_cnt, chosen, chicken_idx+1, ans)

def check_distance(chickens, chosen, chicken_distance, house_cnt):
    heap = []
    for i in chosen:
        heap.extend(chicken_distance[chickens[i]])
    heapify(heap)
    visited = set()
    res = 0
    while heap and house_cnt:
        while heap[0][1:] in visited:
            heappop(heap)
        dist, hx, hy = heappop(heap)
        visited.add((hx, hy))
        res += dist
        house_cnt -= 1
    return res

def main():
    n, m = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(n)]
    chickens, chicken_distance, house_cnt = get_chicken_distance(n, city)
    ans = [int(1e10)]
    bruteforce(n, m, city, chickens, chicken_distance, house_cnt, [], 0, ans)
    print(ans[0])


if __name__ == "__main__":
    main()