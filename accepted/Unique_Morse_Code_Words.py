## https://leetcode.com/problems/unique-morse-code-words/

## given a list of words, turn those into their morse code
## representations, then find out how many unique outputs
## there are.  

## my method is to use a dictionary to transform each letter,
## then do the transformation within a nested list comprehension
## for speed, then finally to return the length of the set.

## gets me 94th percentile in runtime and 85th percentile in
## memory.  complexity is O(number of letters in words); fortunately
## python handles the double for loop very well in a comprehension

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        import string
        letters = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        morse_to_eng = dict(zip(string.ascii_lowercase, letters))
        transformations = [''.join([morse_to_eng[char] for char in w]) for w in words]
        return len(set(transformations))