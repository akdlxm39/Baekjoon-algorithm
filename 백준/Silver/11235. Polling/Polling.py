import sys
input = sys.stdin.readline

def main():
    n = int(input())
    votes = dict()
    for _ in range(n):
        s = input().rstrip()
        if s in votes:
            votes[s] += 1
        else:
            votes[s] = 1
    high_score = 0
    ans = []
    for name, cnt in votes.items():
        if cnt < high_score:
            pass
        elif cnt > high_score:
            ans = [name]
            high_score = cnt
        else:
            ans.append(name)
    print('\n'.join(sorted(ans)))

if __name__ == "__main__":
    main()