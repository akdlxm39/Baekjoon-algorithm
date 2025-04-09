import sys
import math
input = sys.stdin.readline

def distance(x1, y1, z1, x2, y2, z2):
    return ((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)**0.5

def main():
    ax, ay, az, bx, by, bz, cx, cy, cz = map(int, input().split())
    ab = distance(ax, ay, az, bx, by, bz)
    ac = distance(ax, ay, az, cx, cy, cz)
    bc = distance(bx, by, bz, cx, cy, cz)
    if ab+ac==bc or ac+bc==ac:
        ans = min(ac, bc)
    elif ac+bc==ab:
        ans = 0
    else:
        a_theta = math.acos((ab * ab + ac * ac - bc * bc) / (2 * ab * ac))
        b_theta = math.acos((ab * ab + bc * bc - ac * ac) / (2 * ab * bc))
        if a_theta < math.pi / 2 and b_theta < math.pi / 2:
            ans = ac * math.sin(a_theta)
        else:
            ans = min(ac, bc)
    print(ans)

if __name__ == "__main__":
    main()