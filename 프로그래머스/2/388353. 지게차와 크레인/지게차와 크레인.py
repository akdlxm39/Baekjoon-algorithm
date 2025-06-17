def adj_can_fork(n, m, can_fork, deliveried, x, y):
    for dx, dy in [[0,1], [0,-1], [1,0], [-1,0]]:
        nx, ny = x+dx, y+dy
        if not (0<=nx<n and 0<=ny<m): continue
        if deliveried[nx][ny] and not can_fork[nx][ny]:
            can_fork[nx][ny] = True
            adj_can_fork(n, m, can_fork, deliveried, nx, ny)
        else:
            can_fork[nx][ny] = True

def crane(n, m, storage, can_fork, deliveried, request):
    delivery_list = []
    for i in range(n):
        for j in range(m):
            if not deliveried[i][j] and storage[i][j] == request:
                delivery_list.append((i, j))
    for i, j in delivery_list:
        deliveried[i][j] = True
        if can_fork[i][j]: adj_can_fork(n, m, can_fork, deliveried, i, j)
            
    
def fork(n, m, storage, can_fork, deliveried, request):
    fork_list = []
    for i in range(n):
        for j in range(m):
            if can_fork[i][j] and not deliveried[i][j] and storage[i][j] == request:
                fork_list.append((i, j))
    for i, j in fork_list:
        deliveried[i][j] = True
        adj_can_fork(n, m, can_fork, deliveried, i, j)
            
def solution(storage, requests):
    n, m = len(storage), len(storage[0])
    can_fork = [[True]*m]+[[True]+[False]*(m-2)+[True] for _ in range(n-2)] + [[True]*m]
    deliveried = [[False]*m for _ in range(n)]
    for request in requests:
        if len(request) == 1:
            fork(n, m, storage, can_fork, deliveried, request)
        else:
            crane(n, m, storage, can_fork, deliveried, request[0])
    answer = n*m-sum(sum(line) for line in deliveried)
    return answer
    
    