import sys
input = sys.stdin.readline

def main():
    Ax, Ay, Bx, By, Cx, Cy = map(int, input().split())
    lines = [((Ax - Bx) ** 2 + (Ay - By) ** 2) ** 0.5,
             ((Ax - Cx) ** 2 + (Ay - Cy) ** 2) ** 0.5,
             ((Bx - Cx) ** 2 + (By - Cy) ** 2) ** 0.5]
    ABdx, ABdy, BCdx, BCdy = Bx-Ax, By-Ay, Cx-Bx, Cy-By
    if (ABdx==0 and BCdx==0) or (ABdx!=0 and BCdx!=0 and ABdy/ABdx == BCdy/BCdx):
        print(-1)
    else:
        print(2*(max(lines)-min(lines)))

if __name__ == "__main__":
    main()