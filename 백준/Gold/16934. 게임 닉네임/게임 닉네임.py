import sys
input = sys.stdin.readline

class userDB:
    def __init__(self, name=''):
        self.name = name
        self.name_count = 0
        self.next_alpha = dict()

    def add_user(self, name, i=0):
        # return nickname
        if i == len(name):
            self.name_count += 1
            return self.name + (str(self.name_count) if self.name_count > 1 else '')
        if name[i] not in self.next_alpha:
            self.next_alpha[name[i]] = userDB(self.name+name[i])
            nickname = self.name+name[i]
            self.next_alpha[name[i]].add_user(name, i+1)
        else:
            nickname = self.next_alpha[name[i]].add_user(name, i+1)
        return nickname

def main():
    n = int(input())
    users = userDB()
    for _ in range(n):
        s = input().rstrip()
        print(users.add_user(s))

if __name__ == "__main__":
    main()