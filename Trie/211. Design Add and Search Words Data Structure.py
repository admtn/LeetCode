class TrieNode:
    def __init__(self) -> None:
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
        def searchFromHere(start:TrieNode, word_left:str) -> bool:
            cur = start
            for i,c in enumerate(word_left):
                if c == '.':
                    for k in cur.children:
                        if searchFromHere(cur.children[k],word_left[i+1:]):
                            return True
                    return False
                elif c not in cur.children:
                    return False
                else:
                    cur = cur.children[c]
            return cur.end
        return searchFromHere(self.root,word)
                
s = WordDictionary()
s.addWord("bad")
s.addWord("dad")
s.addWord("mad")
print(s.search("pad"))
print(s.search("bad"))
print(s.search(".ad"))
print(s.search("b.."))

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)