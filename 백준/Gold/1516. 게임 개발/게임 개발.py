import sys
from collections import deque
input = sys.stdin.readline

def main():
    n = int(input())
    build_times = [0]*(n+1)
    postrequisite_buildings = [[] for i in range(n+1)]
    prerequisite_buildings = [[] for i in range(n+1)]
    number_of_required_buildings = [0]*(n+1)
    build_queue = deque()
    for i in range(1, n+1):
        build_times[i], *prerequisites = map(int, input().split())
        number_of_required_buildings[i] = len(prerequisites)-1
        if number_of_required_buildings[i] == 0:
            build_queue.append(i)
        prerequisite_buildings[i] = prerequisites[:-1]
        for prerequisite in prerequisites[:-1]:
            postrequisite_buildings[prerequisite].append(i)
    total_times = build_times[:]
    while build_queue:
        cur_building = build_queue.popleft()
        if prerequisite_buildings[cur_building]:
            total_times[cur_building] += max(total_times[i] for i in prerequisite_buildings[cur_building])
        for nxt_building in postrequisite_buildings[cur_building]:
            number_of_required_buildings[nxt_building] -= 1
            if number_of_required_buildings[nxt_building] == 0:
                build_queue.append(nxt_building)
    print(*total_times[1:], sep='\n')


if __name__ == "__main__":
    main()