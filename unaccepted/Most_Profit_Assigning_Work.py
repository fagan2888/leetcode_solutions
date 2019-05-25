## https://leetcode.com/problems/most-profit-assigning-work/

## problem is, given a list of tasks with certain difficulties,
## a list of how much profit we make from each job, and a list of
## how capable each worker is (i.e. how difficult of a task they 
## can complete)

## each worker can only do one job, but each job can be completed
## (and profit made off of) by as many workers as we want

## this solution is too slow, but the general method seems sound
## we first build a lookup table of the max profit you can make 
## from a task given a difficulty (can probably be optimized),
## then we assign each worker a task based on the max profit they 
## can make, then we sum all that up.

## needs some additional work to simplify (too many for loops I 
## think) and speed up, obviously.

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        max_profit_given_difficulty = {}
        for (d, p) in zip(difficulty, profit):
            if True in [max_profit_given_difficulty[other_d]>p for other_d in 
                       max_profit_given_difficulty if other_d <= d]:
                continue
            else:
                max_profit_given_difficulty[d] = p
        
        to_pop = []
        for d in max_profit_given_difficulty:
            if True in [max_profit_given_difficulty[other_d]>max_profit_given_difficulty[d] for
                        other_d in max_profit_given_difficulty if other_d < d]:
                to_pop.append(d)
        for d in to_pop:
            max_profit_given_difficulty.pop(d)
        
        unique_diffs = list(max_profit_given_difficulty.keys())
        unique_diffs.sort()
                
        ## given an ability, get the max profit of an available task
        ## i.e. if we have tasks with diffs of 1 and 3 that make 5 and 10 respectively,
        ## then this should be [0, 5, 5, 10]        
        profit_lookup = []
        
        ds_index = -1
        current_diff = None
        current_profit = 0
        for ii in range(max([unique_diffs[-1], max(worker)])+1):
            if ii < unique_diffs[0]:
                ## no tasks available
                profit_lookup.append(0)
                continue
            
            if ds_index == len(unique_diffs) - 1:
                current_profit = max_profit_given_difficulty[unique_diffs[-1]]
                profit_lookup.append(current_profit)
            
            elif ii == unique_diffs[0]:
                ds_index = 0
                current_diff = unique_diffs[ds_index]
                current_profit = max_profit_given_difficulty[current_diff]
            elif ii == unique_diffs[ds_index+1]:
                ds_index = ds_index + 1
                current_diff = unique_diffs[ds_index]
                current_profit = max_profit_given_difficulty[current_diff]
            profit_lookup.append(current_profit)
                
        output = 0
        for w in worker:
            output += profit_lookup[w]
        return output