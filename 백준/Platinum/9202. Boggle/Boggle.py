import sys
input = sys.stdin.readline
delta = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

class dictionary:
    def __init__(self, word=''):
        self.word = word
        self.is_word : bool = False
        self.next_alpha = dict()

    def add_word(self, word, i = 0):
        if i == len(word):
            self.is_word = True
            return
        if word[i] not in self.next_alpha:
            self.next_alpha[word[i]] = dictionary(self.word + word[i])
        self.next_alpha[word[i]].add_word(word, i+1)

    def get_all_word(self):
        if self.is_word:
            print(self.word)
        for x in self.next_alpha.values():
            x.get_all_word()

def dfs(my_dict:dictionary, board, visited, x, y, word_set):
    if board[x][y] not in my_dict.next_alpha:
        return
    next_dict = my_dict.next_alpha[board[x][y]]
    if next_dict.is_word:
        word_set.add(next_dict.word)
    visited[x][y] = True
    for dx, dy in delta:
        nx, ny = x + dx, y + dy
        if visited[nx][ny]:
            continue
        dfs(next_dict, board, visited, nx, ny, word_set)
    visited[x][y] = False

def main():
    len_to_point = [0, 0, 0, 1, 1, 2, 3, 5, 11]
    my_dict = dictionary()
    for _ in range(int(input())):
        s = input().rstrip()
        my_dict.add_word(s)
    input()
    n = int(input())
    for i in range(n):
        board = [' '*6] + [' ' + input().rstrip() + ' ' for _ in range(4)] + [' '*6]
        visited = [[True]*6]+[[True]+[False]*4+[True] for _ in range(4)]+[[True]*6]
        word_set = set()
        for j in range(1,5):
            for k in range(1,5):
                dfs(my_dict, board, visited, j, k, word_set)
        point = 0
        longest_word = ''
        for word in word_set:
            point += len_to_point[len(word)]
            if len(word) > len(longest_word) or len(word)==len(longest_word) and word<longest_word:
                longest_word = word
        print(point, longest_word, len(word_set))
        if i < n-1:
            input()

if __name__ == "__main__":
    main()