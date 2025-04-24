import sys
from copyreg import constructor

input = sys.stdin.readline

def union(root, num_of_friends, a, b):
    ar, br = find(root, a), find(root, b)
    if ar < br:
        root[br] = ar
        num_of_friends[ar] += num_of_friends[br]
        return num_of_friends[ar]
    elif ar > br:
        root[ar] = br
        num_of_friends[br] += num_of_friends[ar]
    return num_of_friends[br]

def find(root, x):
    if root[x] != x:
        root[x] = find(root, root[x])
    return root[x]

def new_friend(a, b, user_id, id_nums, root, num_of_friends):
    if a not in user_id:
        user_id[a] = id_nums
        root.append(id_nums)
        num_of_friends.append(1)
        id_nums += 1
    if b not in user_id:
        user_id[b] = id_nums
        root.append(id_nums)
        num_of_friends.append(1)
        id_nums += 1
    return id_nums

def main():
    t = int(input())
    for _ in range(t):
        f = int(input())
        user_id, id_nums = dict(), 0
        root, num_of_friends = [], []
        for _ in range(f):
            a, b = input().split()
            id_nums = new_friend(a, b, user_id, id_nums, root, num_of_friends)
            print(union(root, num_of_friends, user_id[a], user_id[b]))

if __name__ == "__main__":
    main()