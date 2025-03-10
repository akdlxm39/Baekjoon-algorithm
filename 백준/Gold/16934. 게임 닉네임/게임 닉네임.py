import sys
input = sys.stdin.readline

def main():
    n = int(input())
    prefix_set = set()
    name_count = dict()
    nicknames = []
    for _ in range(n):
        name = input().rstrip()
        nickname = ''
        for i in range(1, len(name)+1):
            cur_prefix = name[:i]
            if not nickname and cur_prefix not in prefix_set:
                nickname = cur_prefix
            prefix_set.add(cur_prefix)
        if name not in name_count:
            name_count[name] = 0
        name_count[name] += 1
        if not nickname:
            count = name_count[name]
            nickname = name + (str(count) if count > 1 else '')
        nicknames.append(nickname)
    print('\n'.join(nicknames))

if __name__ == "__main__":
    main()