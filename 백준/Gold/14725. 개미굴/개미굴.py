import sys
input = sys.stdin.readline

class Room:
    def __init__(self, name):
        self.name = name
        self.child = []
    def put(self, rooms):
        # if not rooms: return
        for c in self.child:
            if c.name == rooms[0]:
                c.put(rooms[1:])
                break
        else:
            self.child.append(Room(rooms[0]))
            if len(rooms) > 1:
                self.child[-1].put(rooms[1:])

    def get(self, level=0):
        self.child.sort(key = lambda x: x.name)
        result = ''
        for c in self.child:
            result += '--' * level + c.name + '\n'
            if len(c.child) > 0:
                result += c.get(level+1)
        return result

def main():
    n = int(input())
    enter = Room('enter')
    for _ in range(n):
        _, *x = input().split()
        enter.put(x)
    print(enter.get())

if __name__ == "__main__":
    main()