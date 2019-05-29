## https://leetcode.com/problems/longest-palindromic-substring/

## brute-force O(len(s)^2) solution turns out to be (barely) fast 
## enough: iterate over the string, iterate over the rest of the 
## string following, check at each index if any string of this length
## would be a longer palindrome than our current longest then check 
## if we've also hit on a palindrome.  if so, we update our maxes and 
## continue on.

## comes in at 22nd percentile for runtime, though 75th for memory.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s
        
        current_max = 0
        starting_idx = 0
        for ii in range(len(s)):
            for jj in range(ii+1, len(s)+1):
                if jj - ii > current_max and s[ii:jj] == s[ii:jj][::-1]:
                    current_max = jj - ii
                    starting_idx = ii
                    
        return s[starting_idx:starting_idx+current_max]