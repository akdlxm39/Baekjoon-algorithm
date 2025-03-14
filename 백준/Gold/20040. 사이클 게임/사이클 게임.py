import sys
input = sys.stdin.readline

def get_root(roots,u):
    if roots[u] == u:
        return u
    roots[u] = get_root(roots, roots[u])
    return roots[u]

def union_and_checkCycle(roots, u, v):
    ur, vr = get_root(roots, u), get_root(roots, v)
    if ur == vr:
        return True
    elif ur < vr:
        roots[vr] = ur
    else:
        roots[ur] = vr
    return False

def main():
    n, m = map(int, input().split())
    roots = list(range(n))
    ans = 0
    for i in range(1, m+1):
        u, v = map(int, input().split())
        if union_and_checkCycle(roots, u, v):
            print(i)
            break
    else:
        print(0)

if __name__ == "__main__":
    main()