import sys

input = sys.stdin.readline


def get_primes(n):
    primes = [False, False] + [True] * (n - 1)
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            primes[i + i::i] = [False] * (n // i - 1)
    return primes


def matching(nums, connections, match, visited, cur):
    for nxt in connections[cur]:
        if visited[nxt]: continue
        visited[nxt] = True
        if match[nxt] == -1 or matching(nums, connections, match, visited, match[nxt]):
            match[nxt] = cur
            return True
    return False


def main():
    n = int(input())
    nums = list(map(int, input().split()))
    # n = 50
    # nums = list(range(1, n + 1))
    primes = get_primes(2000)
    connections = [[] for _ in range(n)]
    for i in range(n - 1):
        for j in range(i + 1, n):
            if primes[nums[i] + nums[j]]:
                connections[i].append(j)
                connections[j].append(i)
    if sum(x % 2 for x in nums) != n // 2:
        print(-1)
        return
    answers = []
    is_odd = nums[0] % 2
    match = [-1] * n
    for i in range(1, n):
        if nums[i] % 2 != is_odd: continue
        visited = [False] * n
        if not matching(nums, connections, match, visited, i):
            print(-1)
            return

    for i in connections[0]:
        visited = [False] * n
        visited[i] = True
        if match[i] == -1 or matching(nums, connections, match, visited, match[i]):
            answers.append(nums[i])
            match[i] = -1

    print(' '.join(map(str, sorted(answers))) if answers else -1)


if __name__ == "__main__":
    main()
