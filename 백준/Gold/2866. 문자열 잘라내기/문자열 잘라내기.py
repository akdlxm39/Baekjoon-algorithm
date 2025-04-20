import sys
input = sys.stdin.readline

def main():
    r, c = map(int, input().split())
    words = [input().rstrip() for _ in range(r)]
    cwords = sorted(''.join(words[i][j] for i in range(r)) for j in range(c))
    l, r = 0, r-1
    while l <= r:
        m = (l+r)//2
        word_set = set()
        for i in range(c):
            word = cwords[i][m:]
            if word in word_set:
                r = m-1
                break
            word_set.add(word)
        else:
            l = m+1
    print(r)

if __name__ == "__main__":
    main()