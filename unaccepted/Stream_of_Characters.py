## https://leetcode.com/problems/stream-of-characters/

## problem is to return true on a query if and only if the 
## last k characters queried make up a word in the wordlist.

## my solution is just barely too slow, again failing on the 
## last test-case, but it's pretty straightforward to understand
## at least -- we keep track of words in the wordlist by the length
## of that word, which also tells us the longest string of queries 
## that we need to bother continuing to check.

## then each time we query, we update all of the queries that 
## we care about then check if any are in our wordlist.

class StreamChecker:
    def __init__(self, words: List[str]):
        self.words_by_length = {}
        max_l = 0
        for word in words:
            l = len(word)
            if l in self.words_by_length:
                self.words_by_length[l].append(word)
            else:
                self.words_by_length[l] = [word]
            if l > max_l:
                max_l = l
        
        self.previous_queries = []
        self.max_query_length_to_check = max_l

    def query(self, letter: str) -> bool:
        ### add to previous queries
        ### check if added version matches any of my words of that length
        ### and return true if so.
        ### then drop any queries that are now too long
        updated_queries = []
                
        found = False
        for q in  [''] + self.previous_queries:
            new_q = q + letter
            new_l = len(new_q)
            if new_l <= self.max_query_length_to_check:
                updated_queries.append(new_q)
                ### don't need to check more than once per query
                if not found:  
                    if new_l in self.words_by_length.keys():
                        if new_q in self.words_by_length[new_l]:
                            found = True
            ## don't need to check or append if it's longer than any of our words

        self.previous_queries = updated_queries
        return found
                            

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)