import sys
input = sys.stdin.readline

def find(roots, u):
    if roots[u] == u:
        return u
    roots[u] = find(roots, roots[u])
    return roots[u]

def union(roots, u, v):
    ur, vr = find(roots, u), find(roots, v)
    if ur < vr:
        roots[vr] = ur
    else:
        roots[ur] = vr
    return ur == vr

def main():
    n, m = map(int, input().split())
    roots = list(range(n))
    for i in range(1, m+1):
        u, v = map(int, input().split())
        if union(roots, u, v):
            print(i)
            break
    else:
        print(0)

if __name__ == "__main__":
    main()