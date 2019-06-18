## https://leetcode.com/problems/find-smallest-letter-greater-than-target/

## simple solution is among the fastest -- comes in at 81st for 
## both runtime and memory

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        bigger = [l for l in letters if l > target]
        if not len(bigger):
            return min(letters)
        return min(bigger)