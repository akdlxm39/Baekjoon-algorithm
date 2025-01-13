import sys
input = sys.stdin.readline

def main():
    idx = 1
    while idx:
        l = list(map(int, input().split()))
        if l == [0]:
            break
        print(f"Case {idx}: Sorting... done!")
        idx += 1


if __name__ == "__main__":
    main()