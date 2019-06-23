## https://leetcode.com/problems/implement-trie-prefix-tree/

## pretty similar to the Add and Search Word problem, but now 
## I need to be able to check whether any word in the set start
## with an input.  that slows us down significantly since we're 
## doing a double loop...wonder if I can fix that...  couldn't get 
## it working though.

from collections import defaultdict

class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.words = defaultdict(set)
    

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        self.words[len(word)].add(word)


    def search(self, word: str) -> bool:
        """
        Returns if the exact is in the trie.
        """
        return word in self.words[len(word)]
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        if not len(self.words):
            return False
        
        ml = max(self.words.keys())
        for l in range(len(prefix), ml+1):
            if True in [w.startswith(prefix) for w in self.words[l]]:
                return True
        return False
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)