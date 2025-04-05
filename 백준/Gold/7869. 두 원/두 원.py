import sys
import math
input = sys.stdin.readline

def main():
    x1, y1, r1, x2, y2, r2 = map(float, input().split())
    d = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    ans = 0
    if d+r1 <= r2:
        ans = round(r1*r1*math.pi, 3)
    elif d+r2 <= r1:
        ans = round(r2*r2*math.pi, 3)
    elif r1+r2 <= d:
        ans = "0.000"
    else:
        r1_2, r2_2, d_2 = r1*r1, r2*r2, ((x2 - x1)**2 + (y2 - y1)**2)
        theta1 = 2 * math.acos((r1_2+d_2-r2_2)/(2*r1*d))
        theta2 = 2 * math.acos((r2_2+d_2-r1_2)/(2*r2*d))
        ans = round(r1_2*theta1/2 + r2_2*theta2/2 - r1_2*math.sin(theta1)/2 - r2_2*math.sin(theta2)/2, 3)
    print(ans)

if __name__ == "__main__":
    main()