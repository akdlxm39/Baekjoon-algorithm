import sys
input = sys.stdin.readline

def main():
    n, x = map(int, input().split())
    if n <= x <= 26*n:
        # 'A'*n인 문자열로 시작, 남은 x는 (x - n)
        # 'A'를 'Z'로 만들 수 있는 (즉, 25를 더해줄 수 있는 문자의) 개수
        # 남은 x에 25로 나눈 값
        zcnt = (x - n) // 25
        # 'A'문자열과 'Z'문자열 사이에 있는 문자를 제외한 'A'문자열의 길이
        acnt = max(0, n - zcnt - 1)
        # 사이에 들어갈 문자 ('A'부터 'Y'까지 중 하나)
        # x에서 ('A'문자열의 길이)를 빼고, ('Z'문자열의 길이)*26을 뺀 값에 위치한 문자
        remain = x-acnt-zcnt*26
        # 그 값이 0이라면 사이에 존재하는 문자가 없음
        mid = chr(64 + remain) if remain else ''
        print('A'*acnt+mid+'Z'*zcnt)
    else:
        print('!')

if __name__ == "__main__":
    main()