## https://leetcode.com/problems/evaluate-reverse-polish-notation/

## classic problem, classic solution -- use a stack and just 
## follow the algorithm.  only vaguely tricky part is implementing
## division (and getting the order of operators correct).

## comes in at 89th percentile for speed and 50th for memory.

class Solution:
    def division(self, denom, num):
        from math import floor, ceil
        res = num/denom
        if res < 0:
            return int(ceil(res))
        return int(floor(res))
    
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'/': self.division,
                     '+': lambda a, b:  b + a, 
                     '*': lambda a, b:  b * a,
                     '-': lambda a, b:  b - a}
        
        from collections import deque
        stack = deque([int(tokens[0])])
        for ii in range(1, len(tokens)):
            if tokens[ii] in operators:
                stack.append(operators[tokens[ii]](stack.pop(), stack.pop()))
            else:
                stack.append(int(tokens[ii]))
        return stack.pop()