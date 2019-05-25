## https://leetcode.com/problems/reconstruct-original-digits-from-english/

## given a string that consists of jumbled english-language numbers (i.e. 
## oerz or neo for zero or one).  the solution i attempted is to keep 
## iterating while there's a string to iterate over, check for the letters
## of each number, and, if we find them all, replace them with an empty 
## string (i.e. pop them out).  this is clearly sub-optimal though.

class MyString(str):
    def my_index(self, sub):
        try:
            return self.index(sub)
        except ValueError:
            return None
    
    def eliminate_first(self, sub):
        return MyString(self.replace(sub, '', 1))

class Solution:
    def originalDigits(self, s: str) -> str:
        numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        transformer = dict(zip(numbers, [str(ii) for ii in range(10)]))
                           
        string = MyString(s)
        
        output = ""
        while len(string):
            for n in numbers:
                indices = [string.my_index(c) for c in n]
                if None not in indices:
                    output += transformer[n]
                    for c in n:
                        string = string.eliminate_first(c)
                    if not len(string):
                        break
        return output