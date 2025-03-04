import sys
input = sys.stdin.readline

size = 1000000
primes = [False] * 2 + [True] * (size-1)
for i in range(2, int(size**0.5)+1):
    if primes[i] == False:
        continue
    primes[2*i:size+1:i] = [False] * (size//i-1)
primeNums = [x for x in range(1000001) if primes[x]]

T = int(input())
for _ in range(T):
    N = int(input())
    count = 0
    for p in primeNums:
        if p > N//2:
            break
        if primes[N-p]:
            count += 1
    print(count)