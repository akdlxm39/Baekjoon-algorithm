import sys
input = sys.stdin.readline

M = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def main():
    n, l, f = input().split()
    n, l, f = int(n), (int(l[:3]), int(l[4:6]),int(l[7:])), int(f)
    rental = dict()
    fines = dict()
    for _ in range(n):
        s = input().split()
        idx = s[3] + ' ' + s[2]
        _, month, days= map(int, s[0].split('-'))
        hours, minutes = map(int, s[1].split(':'))
        if not(idx in rental and rental[idx]):
            rental[idx] = (month, days + l[0], hours + l[1], minutes + l[2])
        else:
            xmonth, xdays, xhours, xminutes = rental[idx]
            days += sum(M[xmonth:month]) - xdays
            hours -= xhours
            minutes -= xminutes
            m = ((days*24 + hours)*60 + minutes)
            if m > 0:
                fine = m * f
                if s[3] in fines:
                    fines[s[3]]+=fine
                else:
                    fines[s[3]] = fine
            rental[idx] = None
    if fines:
        for k in sorted(fines):
            print(k, fines[k])
    else:
        print(-1)

if __name__ == "__main__":
    main()