## https://leetcode.com/problems/repeated-substring-pattern/

## problem is to check whether a string can be constructed out of 
## some sub-portion of that string, repeated several times.

## we accomplish this by checking all possible substrings 
## within the string that could (by length) be put together
## to get something as long as the original string.  
## then, for each of those strings that we find, we check 
## whether each of the following chunks of the original 
## string of the same length are equal to that substring.

## if we never find a substring that meets the criteria, we 
## return false

## this solution is O(len(s)*len(s)) in worse case scenario,
## but that'll only happen in specifically bad cases -- the 
## first len(s) 
## comes from the outer loop, where we loop over the length
## of the list to check if we can construct substrings of 
## that length, and the inner one comes from a loop over 
## the string to see if the substring of a given length
## is the same as all other portions of the string of that
## same length.  note that we break/return if we hit a 
## success, so the only time we do a len(s) loop in the 
## inner loop is for a substring of length(1), and we 
## only do that once.  note that we also break the inner
## loop if we hit an invalid substirng, so we only get one
## loop over len(s) in the inner, that only happens if the 
## last letter is different from all the rest.

## this is an acceptable answer, but not perfect -- runtime
## comes in at 46th percentile, though memory is at 81st 


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        ### can only be made of a substrings where the remainder of length(s) / len(substring) == 0
        valid_possible_lengths = []
        s_length = len(s)
        for ii in range(1, s_length):
            if s_length % ii == 0:
                sub1 = s[:ii]
                num_substrings = s_length // len(sub1)
                broken = False
                for jj in range(num_substrings):
                    sub2 = s[jj*ii:(jj+1)*ii]
                    if sub1 != sub2:
                        broken = True
                        break
                if not broken:
                    return True
        return False
