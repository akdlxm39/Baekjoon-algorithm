import sys
input = sys.stdin.readline

def main():
    while True:
        N, *histogram = list(map(int, input().split()))
        if N == 0:
            break
        answer = [0]
        solution(N, histogram, answer)
        print(answer[0])
        
def solution(N, A, answer):
    s = []
    for i in range(N):
        while s and A[s[-1]] > A[i]:
            tmp = s.pop()
            answer[0] = max(answer[0], (i-(s[-1]if s else -1)-1)*A[tmp])
        s.append(i)
    while s:
        tmp = s.pop()
        answer[0] = max(answer[0], (N-(s[-1]if s else -1)-1)*A[tmp])

main()