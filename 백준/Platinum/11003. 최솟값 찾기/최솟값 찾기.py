import sys
input = sys.stdin.readline

def main():
    n, l = map(int, input().split())
    nums = list(map(int, input().split()))
    num_dq = [0]*n
    idx_dq = [0]*n
    front = 0
    back = 0
    for i, num in enumerate(nums):
        while back > front and num <= num_dq[back-1]:
            back -= 1
        num_dq[back] = num
        idx_dq[back] = i+l-1
        back += 1
        print(num_dq[front], end=' ')
        if idx_dq[front] == i:
            front += 1

if __name__ == "__main__":
    main()