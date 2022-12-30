# https://leetcode.com/problems/design-add-and-search-words-data-structure/
# 1) Design the basic Trie by creating a TrieNode and having a children attribute with the character as a key.
# 2) For searching, do a dfs search and recursively call the function using a node and the index of the word.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True

    def search(self, word: str) -> bool:

        def dfs(index, node):
            cur = node
            for i in range(index, len(word)):
                c = word[i]
                if c == '.':
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False

                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.end

        return dfs(0, self.root)
