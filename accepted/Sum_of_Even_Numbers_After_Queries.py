## https://leetcode.com/problems/sum-of-even-numbers-after-queries/
## this answer is not particularly fast or good on memory..., coming
## in at around the 19th percentile in terms of runtime
## could probably rework it to use only one dictionary

## main runtime complexity is O(len(queries)) (i.e. the loop).  
## total operations in the loop are 3*O(1), since the only lookup
## is from a hash table (dictionary)

class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        answer = []
        
        ## keep a dictionary of even and odd values, along with a running answer
        even_vals = {idx: val for idx, val in enumerate(A) if val % 2 == 0}
        odd_vals = {idx: val for idx, val in enumerate(A) if idx not in even_vals}
        
        last_answer = None
        for q in queries:
            val, idx = q

            ## if the index I'm told to update is currently even
            ## then I pop it out of that dictionary and note that I 
            ## will subtract that value from the running answer
            if idx in even_vals:
                to_sub = even_vals.pop(idx)
                new_v = to_sub + val

            ## if it's odd, though, then I just pop it out
            else:
                to_sub = 0
                new_v = odd_vals.pop(idx) + val

            ## if my new value is even, then I put it in that dictionary
            ## and I note that I add that value to my running answer
            if new_v % 2 == 0:
                even_vals[idx] = new_v
                to_add = new_v

            ## if it's odd, I add nothing and put this value into my new hash table
            else:
                odd_vals[idx] = new_v
                to_add = 0
            
            ## on first loop, have to compute sum over all values
            if last_answer is None:
                answer.append(sum(v for v in even_vals.values()))

            ## on subsequent loops, just two operations to perform
            else:
                answer.append(last_answer - to_sub + to_add)
            last_answer = answer[-1]
        return answer