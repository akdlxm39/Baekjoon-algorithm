import sys
input = sys.stdin.readline

def divide_and_conquer(n, graph, left, right):
    if left == right:
        return graph[left]
    mid = (left + right) // 2
    left_max = divide_and_conquer(n, graph, left, mid)
    right_max = divide_and_conquer(n, graph, mid+1, right)
    h = min(graph[mid], graph[mid+1])
    mid_max = 2 * h
    li, ri = mid-1, mid+2
    while left <= li and ri <= right:
        if graph[li] >= graph[ri]:
            h = min(h, graph[li])
            li -= 1
        else:
            h = min(h, graph[ri])
            ri += 1
        mid_max = max(mid_max, (ri-li-1)*h)
    while left <= li:
        h = min(h, graph[li])
        li -= 1
        mid_max = max(mid_max, (ri-li-1)*h)
    while ri <= right:
        h = min(h, graph[ri])
        ri += 1
        mid_max = max(mid_max, (ri-li-1)*h)
    return max(left_max, mid_max, right_max)

def main():
    n = int(input())
    graph = [int(input()) for _ in range(n)]
    print(divide_and_conquer(n, graph, 0, n-1))

if __name__ == "__main__":
    main()