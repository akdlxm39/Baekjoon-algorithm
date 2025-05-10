import sys
input = sys.stdin.readline

def update(candy_box, node, left, right, candy, count):
    candy_box[node] += count
    if left == right:
        return
    mid = (left + right) // 2
    if left <= candy <= mid:
        update(candy_box, node*2, left, mid, candy, count)
    elif mid+1 <= candy <= right:
        update(candy_box, node*2+1, mid+1, right, candy, count)

def search(candy_box, node, left, right, rank):
    candy_box[node] -= 1
    if left == right:
        return left
    mid = (left + right) // 2
    if rank <= candy_box[node*2]:
        return search(candy_box, node*2, left, mid, rank)
    else:
        return search(candy_box, node*2+1, mid+1, right, rank-candy_box[node*2])

def main():
    n = int(input())
    candy_box = [0]*2097152
    for _ in range(n):
        command = tuple(map(int, input().split()))
        if command[0] == 1:
            print(search(candy_box, 1, 1, 1000000, command[1]))
        elif command[0] == 2:
            update(candy_box, 1, 1, 1000000, command[1], command[2])

if __name__ == "__main__":
    main()