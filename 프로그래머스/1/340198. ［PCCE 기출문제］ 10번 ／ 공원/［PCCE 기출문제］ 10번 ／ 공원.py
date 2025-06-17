def solution(mats, park):
    n, m = len(park), len(park[0])
    can = [[0]*m for _ in range(n)]
    max_can = 0
    for i in range(n):
        for j in range(m):
            if park[i][j] != "-1": continue
            if i == 0 or j == 0:
                can[i][j] = 1
            else:
                can[i][j] = min(can[i][j-1], can[i-1][j], can[i-1][j-1]) + 1
            max_can = max(max_can, can[i][j])
    answer = max([-1] + [x for x in mats if x <= max_can])
    return answer