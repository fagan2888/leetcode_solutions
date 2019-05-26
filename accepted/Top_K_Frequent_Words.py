## https://leetcode.com/problems/top-k-frequent-words/

## given a list of words, return the k most frequent words

## my solution is to iterate over the list of words and record
## their count using a dictionary (O(n)), then loop through the 
## counts (from high to low) until I reach k at least words total.
## since we're asked to sort the words with the same number of
## appearances by alphabetical order, I append sorted lists for 
## each unique number of appearances.  

## i think the slowest part is the for v in ucounts (worst-case 
## scenario runtime there is still O(len(words)), in the case 
## where all of our counts are distinct), since the internals 
## of that loop include a loop over all the unique words 
## and a sort of the words of that count.  however, all of these
## have worst-cases that are the opposite really -- the sort is 
## only slow if there are a lot of words of the same frequency,
## which would make it unlikely that we have lots of different
## frequencies.

## this is born out by the acceptance -- it comes in at 
## 90th percentile in terms of runtime and still does pretty
## well in terms of memory at 66th percentile

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count_by_words = {}
        for w in words:
            count_by_words[w] = count_by_words.get(w, 0) + 1
        
        uwords = list(count_by_words.keys())
        counts = [count_by_words[w] for w in uwords]
        words_to_return_by_count = []
        
        ucounts = sorted(list(set(counts)))[::-1]
        appended = 0
        for v in ucounts:
            my_words = [uwords[ii] for ii in range(len(uwords)) if counts[ii] == v]
            words_to_return_by_count.append(sorted(my_words))
            appended += len(my_words)
            if appended >= k:
                break
        
        import itertools
        flat_words = list(itertools.chain.from_iterable(words_to_return_by_count))
        
        return flat_words[:k]