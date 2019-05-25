## https://leetcode.com/problems/smallest-rotation-with-highest-score/

## problem is to find the highest "score" of an array under any rotation
## where a rotation is where we shift elements before the k-th index to 
## the end for any k.  score is defined as the number of elements that are
## smaller than their index.

## i tried to do this in a brute-force way, but I think I need to be 
## smarter about it...


class Solution:       
    def rotate_and_score_array(self, k):
        return len([v for (ii, v) in enumerate(self.A[k:] + self.A[:k]) if v <= ii])
    
    def bestRotation(self, A: List[int]) -> int:
        self.A = A
        scores = list(map(self.rotate_and_score_array, range(len(A))))
        max_val = max(scores)
        return scores.index(max_val)
