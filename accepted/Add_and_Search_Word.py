## https://leetcode.com/problems/add-and-search-word-data-structure-design/

## i'm really surprised this solution actually works, but it does 
## really well actually -- 87th percentile for runtime and 91st 
## for memory.  basically it's just a set of lists, separated by 
## the length of the words in the list.  then, when I search, I just
## check for all matching characters (if my input word's character is 
## not a .) for only the words of the same length.

from collections import defaultdict

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.words = defaultdict(list)
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        # words.add(word)
        self.words[len(word)].append(word)
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        for w in self.words[len(word)]:
            if False not in [word[ii] == '.' or word[ii] == w[ii] for ii in range(len(word))]:
                return True
        return False
            
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)