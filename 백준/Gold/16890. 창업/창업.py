import sys
from collections import deque
input = sys.stdin.readline

def main():
    str1, str2 = sorted(input().rstrip()), sorted(input().rstrip(), reverse=True)
    n = len(str1)
    str1, str2 = deque(str1[:(n+1)//2]), deque(str2[:n//2])
    ans = [''] * n
    left, right = 0, n-1
    for i in range(n):
        if i % 2 == 0:
            if not str2 or str1[0] < str2[0]:
                ans[left] = str1.popleft()
                left += 1
            else:
                ans[right] = str1.pop()
                right -= 1
        else:
            if not str1 or str1[0] < str2[0]:
                ans[left] = str2.popleft()
                left += 1
            else:
                ans[right] = str2.pop()
                right -= 1
    print(''.join(ans))

if __name__ == "__main__":
    main()