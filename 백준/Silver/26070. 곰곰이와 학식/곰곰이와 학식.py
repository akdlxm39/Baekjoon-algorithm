import sys
input = sys.stdin.readline

def main():
    bears = list(map(int, input().split()))
    tickets = list(map(int, input().split()))
    ans = 0
    for i in range(5):
        if tickets[i%3] >= bears[i%3]:
            ans += bears[i%3]
            tickets[(i+1)%3] += (tickets[i%3]-bears[i%3])//3
            bears[i%3] = tickets[i%3] = 0
        else:
            ans += tickets[i%3]
            bears[i%3], tickets[i%3] = bears[i%3]-tickets[i%3], 0
    print(ans)

if __name__ == "__main__":
    main()