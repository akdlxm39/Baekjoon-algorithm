import sys
input = sys.stdin.readline

def main():
    n, f = input().rstrip(), int(input())
    num = 0
    for i in range(len(n)-2):
        num*=10
        num+=int(n[i])
        num%=f
    num*=100
    for i in range(0, 100):
        tmp = num+i
        if tmp%f == 0:
            if i < 10:
                print(0,end='')
            print(i)
            break

if __name__ == "__main__":
    main()