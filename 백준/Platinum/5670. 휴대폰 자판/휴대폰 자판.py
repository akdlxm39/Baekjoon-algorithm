import sys
input = sys.stdin.readline

class Trie:
    def __init__(self, word = '', is_word = False, children = None):
        if children is None:
            children = {}
        self.is_word = is_word
        self.word = word
        self.children = children

    def __str__(self, indent = 0):
        res = ''
        if self.is_word:
            res += self.word + '\n'
        for child in self.children.values():
            res += child.__str__(indent + 1)
        return res

    def add(self, word, i = 0):
        while i < len(self.word) and i < len(word):
            if self.word[i] != word[i]: break
            i += 1
        if i < len(self.word) and i < len(word):
            new_children = {self.word[i]: Trie(self.word, self.is_word, self.children),
                            word[i]: Trie(word, True)}
            self.is_word = False
            self.word = word[:i]
            self.children = new_children
        elif i == len(word) and i == len(self.word):
            self.is_word = True
        elif i == len(word):
            new_children = {self.word[i]:Trie(self.word, self.is_word, self.children)}
            self.is_word = True
            self.word = word
            self.children = new_children
        elif i == len(self.word):
            if word[i] in self.children:
                self.children[word[i]].add(word, i)
            else:
                self.children[word[i]] = Trie(word, True)

    def result(self, cnt = 0):
        res = cnt if self.is_word else 0
        key = self.children.keys()
        if not self.is_word and len(key) == 1 and self.word != '':
            res += self.children[tuple(key)[0]].result(cnt)
        else:
            for k in key:
                res += self.children[k].result(cnt + 1)
        return res

def main():
    while True:
        n = input()
        if n == '':
            break
        n = int(n)
        dictionary = Trie()
        for _ in range(n):
            word = input().rstrip()
            dictionary.add(word)
        print(f'{dictionary.result()/n:.2f}')

if __name__ == "__main__":
    main()