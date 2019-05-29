## https://leetcode.com/problems/longest-substring-without-repeating-characters/

## find the length of the longest substring in s that doesn't have any repeating
## characters.

## pretty simple brute-force solution, but it's only O(n^2) at worst, so still not
## too bad.  loop over the string once, checking each character to see if it's in 
## the current batch of characters we're processing.  if it is, we check if that 
## batch is longer than our current longest batch, then reset to drop all characters
## before and including the character that we're now adding that is a repeat.

## comes in at nearly 96th percentile in terms of speed, though only 17th in 
## terms of memory because we keep a copy of the current set of characters --
## could solve it without that by keeping track of a starting and ending index
## instead

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not len(s):
            return 0
        
        max_length = 0
        current_length = 1
        
        current_string = s[0]
        for ii in range(1, len(s)):
            ## this is our slowest step, but we still say below O(n^2)
            last_index = current_string.find(s[ii])
            if last_index >= 0:
                ## found this character in the current string -- reset from that instance on
                max_length = max([len(current_string), max_length])
                current_string = current_string[last_index+1:] + s[ii]
            else:
                current_string += s[ii]
        return max([max_length, len(current_string)])