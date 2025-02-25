import sys
input = sys.stdin.readline

M = [0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

def main():
    n, l, f = input().split()
    n, l, f = int(n), (int(l[:3])*24 + int(l[4:6]))*60 +int(l[7:]), int(f)
    rental = dict()
    fines = dict()
    for _ in range(n):
        s = input().split()
        idx = s[3] + ' ' + s[2]
        _, month, days= map(int, s[0].split('-'))
        hours, minutes = map(int, s[1].split(':'))
        time = ((M[month] + days)*24 + hours)*60 + minutes
        if not(idx in rental and rental[idx]):
            rental[idx] = time + l
        else:
            over = time - rental[idx]
            if over > 0:
                if s[3] in fines:
                    fines[s[3]] += over * f
                else:
                    fines[s[3]] = over * f
            rental[idx] = None
    if fines:
        for k in sorted(fines):
            print(k, fines[k])
    else:
        print(-1)

if __name__ == "__main__":
    main()